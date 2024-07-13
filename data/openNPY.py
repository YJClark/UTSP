import numpy as np

instance = np.load('test_tsp_instance_200.npy')
# print(instance[0])

sol = np.load('test_tsp_sol_200.npy')
print(sol[127])
