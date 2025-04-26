# data_generator.py

import numpy as np

def generate_dummy_data(samples=100, features=10):
    X = np.random.rand(samples, features)
    y = np.random.randint(0, 2, size=samples)  # 0 = healthy, 1 = damaged
    return X, y
