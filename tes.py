import numpy as np

matriksA = np.array([[1,0], [3,2]])
matriksB = np.array([[2,1], [3,6]])

matriksC = matriksA + matriksB
matriksD = matriksA - matriksB

print(matriksC)
print(matriksD)

matriksE = np.dot(matriksA, matriksB)
print(matriksE)

det = np.linalg.det(matriksA)
print(det)