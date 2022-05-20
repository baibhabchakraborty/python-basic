import numpy as np

a = np.array([[1,2,3],[2,0,4],[5,6,7]])
row = a.shape[0]
col = a.shape[1]



for i in range(0,row):
    for j in range(0,col):
        if a[i][j] == 0:
            row0=i
            col0=j

a[row0, :] = 0
a[:, col0] = 0
print(a)