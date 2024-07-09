import random
import time
import sys

# Ordenação

# Invariante de laço
# Propriedade que relaciona as variáveis do algoritmo a cada execução completa do laço

# Selection Sort
# Algoritmo de ordenação baseado em passar sempre o menor valor do vetor para a primeira posição (como o que foi feito em sala de aula com os post-its amarelos)

def selection_sort(l):
    for i in range(len(l)):
        menor_indice = i    # Guarda o índice do menor elemento
        for j in range(i+1, len(l)):    
            if l[j] < l[menor_indice]:  # Compara o elemento atual l[j] pelo elemento na posição menor_indice        
                menor_indice = j    # Troca utilizando tupla entre o elemento na posição menor_indice e o elemento na posição i
        l[menor_indice], l[i] = l[i], l[menor_indice]
    
# Bubble Sort
# Algoritmo de orgenação que percorre a lista várias vezes comparando pares de elementos adjacentes e trocando-os de lugar se estiverem fora de ordem, até que nenhum elemento precise ser trocado
# Deixa o vetor mais ordenado a cada iteração
# É um algoritmo mais lento
        
def bubble_sort(l): 
    for i in range (len(l)):
        flag = 0
        for j in range(len(l)-1, i, -1):    # Percorre os elementos da lista a serem comparados e trocados (de trás para frente)
            if l[j-1] > l[j]:   # Se o penúltimo elemento da lista l[j-1] for maior que o elemento atual l[j] (último da lista)
                l[j-1], l[j] = l[j], l[j-1] # Realiza a troca dos elementos
                flag = 1
        if (flag == 0): # Se ocorrer uma iteração que não há alteração de elementos (flag == 0) a lista já está ordenada
            break

# Insertion Sort
# O algoritmo itera pela lista, iniciando no segundo elemento e compara com aqueles à sua esquerda na lista ordenada, deslocando elementos maiores à direita
# É mais rápido que o Selection Sort se a lista já estiver um pouco ordenada
# Também funciona melhor para listas menores

def insertion_sort(l):
    for i in range (1, len(l)):  # Considera que o primeiro elemento está ordenado
        j = i 
        valor = l[i]
        while j > 0 and l[j-1] > valor:
            l[j] = l[j-1]
            j = j-1
        l[j] = valor

# Merge
# Utiliza duas listas já ordenadas para formar uma terceira lista, comparando os elementos de ambas e inserindo o menor
# É preciso ter uma variável i para iterar pela lista 1 e uma variável j para iterar pela lista 2, comparando-os

def merge(ord_l1, ord_l2):
    i = 0 
    j = 0
    lista_resultado = []
    while i < len(ord_l1) and j < len(ord_l2):
        if ord_l1[i] <= ord_l2[j]:
            lista_resultado.append(ord_l1[i])
            i = i + 1
        else:
            lista_resultado.append(ord_l2[j])
            j = j + 1
    # Caso sobre elementos em alguma das listas eles são apenas copiados para a lista 3 pois já estão ordenados:
    while i < len(ord_l1):
        lista_resultado.append(ord_l1[i])
        i = i + 1
    while j < len(ord_l2):
        lista_resultado.append(ord_l2[j])
        j = j + 1
    return lista_resultado

# Merge Sort
# Utiliza a função merge para ordenar a lista
# É o algoritmo de ordenação mais rápido apesar de gastar memória adicional

def merge_sort(l):
    if len(l) == 1:
        return l
    meio = int(len(l)/2)    # Divide uma lista em duas metades
    l1 = l[0:meio]
    l2 = l[meio:]
    # Organiza as metades recursivamente
    l1 = merge_sort(l1) 
    l2 = merge_sort(l2)
    return merge(l1, l2)

if __name__ == "__main__":
    
    # Rodar no terminal python aula8.py + nome da lista (arquivo externo dentro da mesma pasta)
    # f = open(sys.argv[1], "r")
    # loriginal = f.read().split()

    # l = loriginal.copy()
    # start_time = time.time()
    # selection_sort(l)
    # end_time = time.time()
    # print('O selection_sort demorou ' + str(end_time - start_time))

    # l = loriginal.copy()
    # l = [random.randint(0,2**32) for i in range(8000)]
    # start_time = time.time()
    # insertion_sort(l)
    # end_time = time.time()
    # print('O insertion_sort demorou ' + str(end_time - start_time))


    # Testes com listas geradas aleatoriamente
    random.seed(42)
    l = [random.randint(0,2**32) for i in range(8000)]
    start_time = time.time()
    selection_sort(l)
    end_time = time.time()
    print('O selection_sort demorou ' + str(end_time - start_time))

    random.seed(42)
    l = [random.randint(0,2**32) for i in range(8000)]
    start_time = time.time()
    bubble_sort(l)
    end_time = time.time()
    print('O bubble_sort demorou ' + str(end_time - start_time))

    random.seed(42)
    l = [random.randint(0,2**32) for i in range(8000)]
    start_time = time.time()
    insertion_sort(l)
    end_time = time.time()
    print('O insertion_sort demorou ' + str(end_time - start_time))

    random.seed(42)
    l = [random.randint(0,2**32) for i in range(8000)]
    start_time = time.time()
    merge_sort(l)
    end_time = time.time()
    print('O merge_sort demorou ' + str(end_time - start_time))


    # Teste Merge
    # l1 = [ 1, 3, 5, 7, 9]
    # l2 = [2, 4, 6, 8, 10, 12]
    # l = merge(l1, l2)
    # print(l) 

    # Teste Merge Sort
    # l = [7, 3, 5, 1]
    # l = merge_sort(l)
    # print(l)