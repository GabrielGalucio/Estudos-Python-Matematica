# Podemos considerar escalares, vetores e matrizes como tensores generalizados por
# uma rank referente a cada tipo de estrutura, sendo assim:
# Escalares -> rank 0
# Vetores ->   rank 1
# Matrizes ->  rank 2

# Tensores possuem 3 dimenoes K, M e N e pode ser considerado como uma coleção de matrizes

# Demonstrando a criação de 1 tensor com duas matrizes

# Importando biblioteca NumPy
import numpy as np

# Criando as duas primeiras matrizes
m1 = np.array([[10,20,30],[40,50,60]])
m2 = np.array([[30,20,10],[60,50,40]])
print(m1)
print(m2)

# Depois criamos uma matri "t"(Tensor)
t = np.array([m1,m2])
print(t)

# Ou poderiamos criar manuamente um tensor
t_manual = np.array([ [[10,20,30],[40,50,60]],  [[70,80,90],[91,92,93]] ])
print(t_manual)