import random
import time
import sys
import math

# Counting Sort
# Ordenação estável
# Nível de Complexidade: O(n)
# É preciso saber o maior valor do vetor

def counting_sort(A, maior_valor):    # maior_valor é o maior elemento do vetor que será ordenado
    C = [0 for i in range(maior_valor+1)]
    B = [-1 for i in range(len(A))]
    for a in A :    # Para cada valor/elemento a no vetor A
        C[a] = C[a] + 1
    for i in range(1, maior_valor+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B
        
# Ordena de acordo com determinado dígito (começando pela dezena)
# 482  481  341
# 481  341  352
# 341  482  481
# 352  352  482
def counting_sort_digito(A, d):
    C = [0 for i in range(10)]
    B = [-1 for i in range(len(A))]
    for a in A :    
        digito_significativo = (a // d) % 10  # // é uma divisão inteira
        C[digito_significativo] += 1
    for i in range(1, 10):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        digito_significativo = (A[j] // d) % 10 
        posicao = C[digito_significativo] - 1
        B[posicao] = A[j]
        C[digito_significativo] -= 1
    return B

def radix_sort(lista, D):
    for d in range(D):
        lista = counting_sort_digito(lista, 10**d)
    return lista

# Bucket Sort
# Cria N baldes para cada elemento no vetor A
# Depois ordena individualmente cada balde com Insertion Sort
def bucket_sort(A):
    # Ordena os elementos em baldes
    tamanho = len(A)
    B = [[] for i in range(tamanho)]
    for a in A:
        pos = math.floor(a * tamanho)
        B[pos].append(a)
    for i in range(0, tamanho):
        insertion_sort(B[i])
    L = []
    for i in range(0, tamanho):
        for b in B[i]:
            L.append(b)
    return L

def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list
        
def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    mid_point = int(len(unsorted_list)/2)
    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]
    
    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)
    
    return merge(half_a, half_b)
    
def insertion_sort(l):
    for index in range(1, len(l)):
        search_index = index
        insert_value = l[index]
        while search_index > 0 and l[search_index-1] > insert_value:
            l[search_index] = l[search_index-1]
            search_index -= 1
        l[search_index] = insert_value

if __name__ == "__main__":

    # Teste Counting Sort
    # l = [2, 0, 3, 4, 0, 2]
    # l = counting_sort(l, 4)
    # print(l)

    # Teste Counting Sort Dígito 
    # l = [481, 452, 351, 282]
    # l = counting_sort_digito(l, 1)  
    # l = counting_sort_digito(l, 10)
    # l = counting_sort_digito(l, 100)
    # print(l)

    # Teste Bucket Sort 
    random.seed(42)
    loriginal = [random.random() for i in range(300_000)]
    lordenado = loriginal.copy()
    lordenado.sort()
    l = loriginal.copy()
    starttime = time.time()
    l = bucket_sort(l)
    print("Elapsed Time in Bucket Sort: " + str(time.time() - starttime))
    print(l == lordenado)

    random.seed(42)
    loriginal = [random.randint(0, 2**18) for i in range(300_000)]
    lordenado = loriginal.copy()
    lordenado.sort()

    l = loriginal.copy()
    starttime = time.time()
    l = merge_sort(l)
    print("Elapsed Time in Merge Sort: " + str(time.time() - starttime))
    print(l == lordenado)

    l = loriginal.copy()
    starttime = time.time()
    l = counting_sort(l, 2**18)
    print("Elapsed Time in Counting Sort: " + str(time.time() - starttime))
    print(l == lordenado)

    # Teste Radix Sort
    l = loriginal.copy()
    starttime = time.time()
    l = radix_sort(l, 6)
    print("Elapsed Time in Counting Sort: " + str(time.time() - starttime))
    print(l == lordenado)   