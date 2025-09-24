import multiprocessing as mp
from multiprocessing import Pool
import time
import math

N = 50000000

def cube(x):
    return math.sqrt(x)

PROCESSES = mp.cpu_count()

if __name__ == "__main__":
    # first way, using multiprocessing
    start_time = time.perf_counter()
    with Pool(processes=PROCESSES) as pool:
      result = pool.map(cube, range(10,N))
    finish_time = time.perf_counter()
    print("Program finished in {} seconds - using multiprocessing".format(finish_time-start_time))
    print("---")
    # second way, serial computation
    start_time = time.perf_counter()
    result = []
    for x in range(10,N):
      result.append(cube(x))
    finish_time = time.perf_counter()
    print("Program finished in {} seconds".format(finish_time-start_time))

# import time
# import numpy as np
# import multiprocessing as mp
    

# def howmany_within_range(row, minimum, maximum):
#         count = 0
#         for n in row:
#             if minimum <= n <= maximum:
#                 count = count + 1
#         return count
    

# if __name__ ==  '__main__':

#     # Prepare data
#     np.random.RandomState(100)
#     arr = np.random.randint(0, 10, size=[20000000, 5])
#     data = arr.tolist()
#     data[:5]
    
#     # # Step 1: Init multiprocessing.Pool()
#     # pool = mp.Pool(mp.cpu_count())
#     # time_start = time.time()
#     # # Step 2: `pool.apply` the `howmany_within_range()`
#     # results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
#     # print(results[:10])
#     # time_end = time.time()
#     # print(time_end - time_start)
#     # # Step 3: Don't forget to close
#     # pool.close()
    
#     def apply_async_callback(row, minimum, maximum):
#         time_start = time.time()
#         PROCESSES = mp.cpu_count()
#         with mp.Pool(processes=PROCESSES) as pool:
#             results = [pool.apply(howmany_within_range, args=(row, minimum, maximum)) for row in data]
#         time_end = time.time()
#         print(time_end - time_start)
    
#     for row in data:
#         apply_async_callback(row, 4, 8)
    
    
