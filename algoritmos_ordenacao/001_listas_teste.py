import random
from sorting import selecao_ordenacao

any_numbers = random.sample(range(1, 1000), 42)
already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 32, 34, 76, 40, 42, 87, 99, 112]
inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 29, 28, 22, 16, 8, 6, 5, 3, 1]
repeated = [7, 7, 7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 4, 5, 4, 5, 7, 1]

if __name__ == "__main__":
    lista01 = any_numbers
    print(lista01)
    selecao_ordenacao(lista01)
    print("\n Ordenado:")