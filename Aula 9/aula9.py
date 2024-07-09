import random
import time

# Ordenação

# Partition ou Partição
# l[i:j] < Pivot
# l[j:k] > Pivot
# l[k: ] 

# < P | > P | Não particionado
#  i     j           k 

# Escolho alguém da lista para ser Pivot

def partition(l, first, last):  # first é o primeiro da lista e last o último
    r = random.randint(first, last) # Escolhe aleatoriamente um Pivot e o insere na primeira posição
    l[first], l[r] = l[r], l[first]
    pivot = l[first]
    j = first + 1
    for k in range(first + 1, last + 1):
        if l[k] < pivot:
            j = j + 1
            # Também é preciso trocar com o último da primeira partição
            l[k], l[j-1] = l[j-1], l[k]
    l[first], l[j-1] = l[j-1], l[first]
    return j-1  # Para saber a posição do Pivot e poder ordenar as outras partes

# Mais rápido que o Merge Sort 
def quick_sort(l, first, last):
    # print(l[first:last+1])
    if first >= last:
        return
    pivot = partition(l, first, last)
    # Ordenar a primeira parte l[first:p-1] 
    quick_sort(l, first, pivot-1)
    # Ordenar a segunda parte l[p+1:last]
    quick_sort(l, pivot+1, last)
    # Pivot já estará na posição certa
    return

if __name__ == "__main__":

    # Deve resultar em: menores que Pivot do lado direito e maiores que o Pivot do lado esquerdo
    l = [30, 99, 91, 7, 71, 2, 37, 21, 13]
    quick_sort(l, 0, len(l)-1)   # Ordena do 0 até o tamanho da lista (último)
    print(l)

    random.seed(42)
    l = [random.randint(0,2**32) for i in range(8000)]
    start_time = time.time()
    quick_sort(l, 0, len(l)-1)
    end_time = time.time()
    print('O quick_sort demorou ' + str(end_time - start_time))