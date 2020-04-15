# Conforme orientação do documento 003_Operacoes_Matrizes.py podemos observar que a ope
# ração com matrizes só pode ser realziada caso as matrizes tenhas as mesmas dimensões.

# Porem há uma exceção, por conta de matrizes que podem ser realizadas em Python e em ou
# tras linguagens de programação, podemos adicionar escalares a vetores e matrizes

# Importando biblioteca
import numpy as np

# Criando mais modelos de matrizes
m1 = np.array([[10,20,30],[40,50,60]])
m2 = np.array([[30,20,10],[60,50,40]])
v1 = np.array([5,4,3,2,1])
v2 = np.array([1,2,3,4,5])

# Adicionando  1 a matriz m1
# Observe que foi somando +1 em cada elemento da matriz
print(m1 + 1)

# Podemos realizar a mesma coisa em um vetor
print(v1 + 1)

# É imporrante ressaltar isso pois na matemárica esse tipo de operação NÃO É POSSÍVEL

