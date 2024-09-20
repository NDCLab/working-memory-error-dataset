import os
import pandas as pd
import numpy as np
import scipy.stats as stats
import ast
from scipy.stats import norm, uniform
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from math import pi
from itertools import combinations
import re
import multiprocessing as mp
from multiprocessing import Pool
import time
from tqdm import tqdm
PROCESSES = mp.cpu_count()


def calculate_rel(r2, preds):
    rel = r2 * np.sum((preds - np.mean(preds))**2) / len(preds)
    return rel

def run_optimization(x_data, y_data, bounds, n_iterations=10):
    best_params = None
    best_r2 = -np.inf  # Initialize to a very low value
    
    for _ in range(n_iterations):
        # Random initial parameters within the bounds
        initial_params = [np.random.uniform(low, high) for low, high in zip(bounds[0], bounds[1])]
        
        try:
            # Fit the model
            fit_params, _ = curve_fit(model, x_data, y_data, p0=initial_params, bounds=bounds, nan_policy='omit')
            preds = model(x_data, *fit_params)
            # Calculate R² value
            try:
                r2 = r2_score(y_data, preds)
            except:
                r2 = np.nan
            # print(np.round(r2, 2))
            # Calculate Rel value
            try:
                rel = calculate_rel(r2, preds)
            except:
                rel = np.nan
            
            # Keep the best fit
            if not np.isnan(r2):
                if r2 > best_r2:
                    best_r2 = r2
                    best_params = fit_params
                    best_rel = calculate_rel(r2, preds)
            else:
                best_r2 = r2
                best_params = fit_params
                best_rel = rel
                
        except RuntimeError:
            # Handle the case where the fit doesn't converge
            continue
    
    return best_params, best_r2, best_rel  # Return the best R² and corresponding parameters


# Define the model function based on the equation
def model(x, # vector of time samples
          a_lf, # lf cosine wave amplitude in perfornance units
          b_lf, # lf sine wave amplitude in perfornance units
          omega_lf, # lf wave frequency
          a_hf, # hf cosine wave amplitude in perfornance units
          b_hf, # hf sine wave amplitude in perfornance units
          omega_hf, # hf wave frequency
          c, # constant in performance units
         ):
    return (a_lf * np.cos(2*pi*omega_lf * x) + b_lf * np.sin(2*pi*omega_lf * x) +
            a_hf * np.cos(2*pi*omega_hf * x) + b_hf * np.sin(2*pi*omega_hf * x) + c)

def bootstrap_individual_stats(agg_dfs, n_bootstraps=10, n_iterations=10):
    bootstrap_results = []

    for p_data in tqdm(agg_dfs):
        participant_results = []
        y_data = p_data[output_var].to_numpy()
        x_data = p_data['binned_jitter'].to_numpy()
        N = len(x_data)

        for _ in tqdm(range(n_bootstraps)):
            # Generate a bootstrapped sample by resampling with replacement
            bootstrap_indices = np.random.choice(np.arange(N), size=N, replace=True)
            x_bootstrap = x_data[bootstrap_indices]
            y_bootstrap = y_data[bootstrap_indices]

            # Run the optimization on the bootstrapped data
            best_fit_params, best_r2, best_rel = run_optimization(x_bootstrap, y_bootstrap, bounds, n_iterations=n_iterations)

            # Store the result
            participant_results.append((best_fit_params, best_r2, best_rel))

        bootstrap_results.append(participant_results)

    return bootstrap_results

    
if __name__ == "__main__":
    # first way, using multiprocessing
    output_var = "similarity"
    # Define bounds for the parameters
    if output_var == "similarity":
        bounds=([-1, -1, -2, -1, -1, 3, -2],  # Lower bounds
                [1, 1, 2, 1, 1, 13, 2])
    elif output_var == "hr":
        bounds=([-0.5, -0.5, -2, -0.5, -0.5, 3, -1],  # Lower bounds
                [0.5, 0.5, 2, 0.5, 0.5, 13, 1])
    agg_dfs = []
    for i in range(20):
        agg_dfs.append(pd.read_csv(f"/Users/fzaki001/Documents/DA/wme-face-jitter/{i}.csv"))

    start_time = time.perf_counter()
    with Pool(processes=PROCESSES) as pool:
      result = bootstrap_individual_stats(agg_dfs)
    finish_time = time.perf_counter()
    print("Program finished in {} seconds - using multiprocessing".format(finish_time-start_time))
    print("---")
    # second way, serial computation
    start_time = time.perf_counter()
    result = []
    for x in agg_dfs:
      result.append(bootstrap_individual_stats([x]))
    finish_time = time.perf_counter()
    print("Program finished in {} seconds".format(finish_time-start_time))