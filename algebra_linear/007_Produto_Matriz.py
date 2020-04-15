# Importando biblioteca
import numpy as np

# Vamos aplicar mais métodos de mutiplicação da matriz
m1 = np.array([[1,2,3,4],[5,6,7,8]])
print(m1 * 2)


# Encontrando o produto escalar das matrizes

A = np.array([[1,2,3],[5,6,7]])
B = np.array([[1,2],[3,4],[5,6]])
print(A.shape)
print(B.shape)

print(np.dot(A,B))

