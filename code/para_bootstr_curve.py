import numpy as np
import pickle
import re
import os
from tqdm import tqdm
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from math import pi
import multiprocessing as mp
from multiprocessing import Pool

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

def fit_curve_bootstr(subjects, n_iterations=10, output_var="similarity"):
    if output_var == "similarity":
            bounds=([-1, -1, -2, -1, -1, 3, -2],  # Lower bounds
                    [1, 1, 2, 1, 1, 13, 2])
    elif output_var == "hr":
            bounds=([-0.5, -0.5, -2, -0.5, -0.5, 3, -1],  # Lower bounds
                    [0.5, 0.5, 2, 0.5, 0.5, 13, 1])
    
    for df_var in ["acc", "congruent"]:
        for condition in [0, 1]:
            participants_results = {"sub": [],  "results": []}
            for sub in subjects:
                print(f"Fitting curves to bootstrapped data of sub-{sub}...")
                individual_results = []
                p_matrix = np.load(f"{npy_save_path}raw/sub-{sub}_{output_var}_{df_var}_{condition}.npy")
                for i in tqdm(range(p_matrix.shape[0])):
                    x_data = p_matrix[i, :, 0]
                    y_data = p_matrix[i, :, 1]
                    best_fit_params, best_r2, best_rel = run_optimization(x_data, y_data, bounds, n_iterations=n_iterations)
                    individual_results.append((best_fit_params, best_r2, best_rel))
                participants_results["sub"].append(sub)
                participants_results["results"].append(individual_results)
            
            with open(f"{npy_save_path}res_curve/{output_var}_{df_var}_{condition}.pkl", "wb") as tf:
                pickle.dump(participants_results, tf)

npy_save_path = "/Users/fzaki001/Documents/working-memory-error-dataset/derivatives/face-jitter/behavior/bootstrap/"
pattern = re.compile(r'sub-(\d+)')
subjects = sorted(list(set([pattern.search(file).group(1) for file in os.listdir(npy_save_path+"raw/")])))

PROCESSES = mp.cpu_count()

if __name__ == "__main__":
    with Pool(processes=PROCESSES) as pool:
        pool.map(fit_curve_bootstr, [subjects])