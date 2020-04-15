# Importando biblioteca

import numpy as np

# Todas as regras acima se aplicam também em matrizes


# Criando mais modelos de matrizes
m1 = np.array([[10,20,30],[40,50,60]])
m2 = np.array([[30,20,10],[60,50,40],[70,80,90]])
v1 = np.array([5,4,3,2,1])
v2 = np.array([1,2,3,4,5])
e1 = np.array([2])

# Para multiplicar escalares, vetores ou matrizes os mesmos devem ter o mesmo comprimento e
# ao realizar esse tipo de operação, podemos obter 2 tipos de valores: o "ponto" ou produto
# interno ou obter o "externo" ou "tensor". Neste caso vamos trabalhar co  o produto pontual
# ou seja o "ponto" -> "dot"

# Na soma de matrizes, comamos os produtos correspodentes e depois somamos cada um deles.
# Podemos utilizar o método dot() oferecido pela biblioteca do NumPy, lembre-se é importan
# tante ter essa biblioteca.

print(np.dot(v1,v2))
print(np.dot(m1,m2))
