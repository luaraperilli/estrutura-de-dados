import random
import time

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

if __name__ == "__main__":
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
