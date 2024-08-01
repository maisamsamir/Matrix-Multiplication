import numpy as np
mat1 = np.random.randint(0, 11, (2, 4))
mat2 = np.random.randint(0, 11, (4, 2))
result = np.dot(mat1, mat2)
print("mat 1:")
print(mat1)

print("\nmat 2:")
print(mat2)

print("\nans:")
print(result)