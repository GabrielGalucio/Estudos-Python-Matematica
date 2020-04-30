# ORDENAÇÃO POR SELEÇÃO

# Uma primeira idéia de selection sorte é verificar o maior ou menor elemento de uma lista
# não ordenada e começa a ordenar. DÃ! ou seja, pega o primeiro elemento (maior ou menor) e
# coloca na ordem, e repete até pegar todos os elementos de uma lista e os colocar em ordem

# Considere uma lista:
# Os números serão ordenados de ordem crescente sempre substituindo a posição de acordo em
# que se vai identificando o menor valor possivel, até formarem uma lista ordenada.
 
# lista_versao0 = [7, 8, 3, 4, 1, 5]
# lista_versao1 = [1, 8, 3, 4, 7, 5]
# lista_versao2 = [1, 3, 8, 4, 7, 5]
# lista_versao3 = [1, 3, 4, 8, 7, 5]
# lista_versao4 = [1, 3, 4, 5, 7, 8]

# 1- Identificar o menor elemento de uma lista

# lista01 = [7,5,1,8,3,6,2]


def selecao_ordenacao(lista):                       # 2. Cria-se uma função para realizar o selection sort = seleção por ordenação
    n = len(lista)                                  # 1. Cria-se uma variavel com metodo len(para valer o tamanho da lista)
    for j in range(n-1):                            # 3. Cria-se uma variavel J para alocar o valor mínimo
        index_minimo = j                            # 1. Cria-se uma variavel com o primeiro valor da lista para inicio do if
        for i in range(j, n):                       # 1 .Andar pela lista com o index i com o tamanho dela n
            if lista[i] < lista[index_minimo]:      # 1. SE index for menor que o valor posicionado [x] no caso começa com o 1 item da lista
                index_minimo = i                    # 1 .Se verdadeiro, o valor minimo assume o valor em que o index está na lista no momento
        if lista[j] > lista[index_minimo]:          # 3. Cria-se uma verificação para a troca, quem está na posição J pelo valor_minimo
            var_auxiliar = lista[j]                 # 3. Cria-se uma variavel auxiliar para pegar o valor contido em uma das extremidades
            lista[j] = lista[index_minimo]          # 3. Coloca na posição J o valor que estava no index_minimo
            lista[index_minimo] = var_auxiliar      # 3. Coloca no index_minimo o valor contido na var_auxiliar que foi usada so para não perder esse valor inicial

# print(valor_minimo)                                   # 1 .No final disso tudo, o valor minimo tem que ser o menor elemento encontrado na lista

# 1. Cria-se uma estrutura que pega o valor mínimo de uma lista, mas isso não 
#    é o sufificente, é necessário pegar esse elemento e reposicionar ele no 
#    novo espaço, conforme definição de ordenação [ORDENAÇÃO POR SELEÇÃO] e repetir isso

# 2. Cria-se uma função para realizar o algoritmo de seleção por ordenação

# 3. Cria-se uma estrutura para alocar o valor minimo e realizar a sua troca

# 4. É necessário tranformar a variavel J em uma variante

