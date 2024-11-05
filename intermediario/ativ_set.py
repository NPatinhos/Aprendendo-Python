"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    # 0
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],     # 1
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],     # 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],     # 3
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],    # 4
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],     # 5
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],  # 6
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],     # 7
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],    # 8 
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],     # 9 
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],     # 10
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],    # 11
]
def lista_set(lista):
    lista_setada = []
    for numero in set(lista):
        lista_setada.append(numero)
    return lista_setada
        
def ordena_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

def conta_idx(lista):
    num_repetido = 10
    idx_repetido = 10
    for i, num in enumerate(lista):
        idx = 0 
        for posic, j in enumerate(lista[i+1:]):
            idx+=1
            if num == j:
                #print(num, idx)
                if (posic + i + 1) < idx_repetido:
                    num_repetido = num
                    idx_repetido = posic+i+1
                break
    print(num_repetido)

for posicao, lista in enumerate(lista_de_listas_de_inteiros):
    print(f'lista {posicao}:')

    if ordena_lista(lista) == lista_set(lista):
        print('-1')
    else:
        conta_idx(lista)
        