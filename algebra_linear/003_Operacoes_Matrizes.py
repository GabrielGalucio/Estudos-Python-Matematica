# Para realizar operaçõe scom matrize,s a unica orientação é que as matrizes
# possueam as mesma dimensões


# Importando biblioteca NumPy
import numpy as np

# Criando as duas primeiras matrizes
m1 = np.array([[10,20,30],[40,50,60]])
m2 = np.array([[30,20,10],[60,50,40]])
print(m1)
print(m2)

# Facilmente podemos somar as matrizes
print(m1 + m2)
print(m1 - m2)

# Podemos realizar a mesma coisa com vetores
v1 = np.array([5,4,3,2,1])
v2 = np.array([1,2,3,4,5])
print(v1 + v2)
print(v1 - v2)