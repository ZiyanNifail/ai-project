import numpy as np
import pandas as pd



X = np.arange(0, 10, 0.1)
y = X ** 2

data = pd.DataFrame({'X': X, 'y': y})

print(data.head())