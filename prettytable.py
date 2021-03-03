import tableprint as tp
import numpy as np

data = np.random.randn(10, 3)
coluna = ['Column A', 'Column B', 'Column C']

tp.table(data, coluna)