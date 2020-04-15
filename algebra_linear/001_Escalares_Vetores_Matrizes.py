# Demonstrando algumas fromas de delcaração de escalares, vetores e matrizes em Python

# Importando a biblioteca NumPy que já vem com os pacotes necessários de calculos matemáticos
import numpy as np

# 1- ESCALARES
# Vamos começar com a declaração de um scalar, que pode ser representado como uma decla
# ração de variavel simples

variavel01 = 5
print(variavel01)

# 2- VETORES
# Para representar o vetor usamos sitaxe da biblioteca NumPy
#
# v = [5]
#     [2]
#     [4]
v = np.array([5, 2, 4])
print(v)

# 3 - MATRIZES
# Para representar o vetor usamos sitaxe da biblioteca NumPy
#
# V = [5, 2, 4]
#     [6, 7, 8]
#
m = np.array([[5,2,4],[6,7,8]])
print(m)

# Então, podemos verificar o tipo de variavel que contém a matriz com o método type()
print(type(v)) # É informado que é um tipo array de NumPy -> Array de 1 dimensão 1D
print(type(m)) # É informado que é um tipo array de NumPy -> Array de 2 dimensões 2D

# 3- ESCALARES
# Para deixar no mesmo tipo, podemos também atribuir a sintaxe do NumPy a variavel que
# emula um escalar s = 5
s = np.array([5])
print(type(s))

# Com o método .shape() podemos verificar as formas das matrizes que criamos
print(m.shape)
print(v.shape)
print(s.shape)

# Criando uma coluna em um vetor
v.reshape(3,1)
print(v)
v.reshape(1,3)
print(v)