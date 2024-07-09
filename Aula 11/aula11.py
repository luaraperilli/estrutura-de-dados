# MAX-HEAP:
# Um heap é uma estrutura de dados que é uma árvore binária quase completa (todos os níveis estão preenchidos exceto o último)
# Elemento pai é sempre maior que os filhos
# No último nível os elementos à esquerda são preenchidos primeiro (crescimento ordenado)
# Com o crescimento ordenado é possível definir como um vetor
# Está sempre bem balanceada 

# Exemplo:
#        (99)
#    (81)    (71)
# (7)    (11)    (10)
# É igual ao vetor:
# |99|81|71|7|11|10|

# Caso algum elemento não esteja balanceado:
# Função sobe_heap -> verifica se o elemento i precisa subir recursivamente (troca com o maior dos filhos)
# Função desce_heap -> veriica se o elemento i precisa descer recursivamente (troca com o maior do filhos)

# Para calcular o filho esquerdo de i -> esq(i) = 2*1 + 1 
# Para calcular o filho direito de i -> esq(i) = 2*1 + 2
# Para calcular o pai de i -> pai(i) = i-1/2

# Complexidade:
# Inserir O(log n)
# Remover O(log n)
# Pick O(1)

# Ordenação: 
# Função extrai_max -> extrai o maior elemento (raiz) e o insere num vetor recursivamente até o menor elemento (fim a árvore)

def desce_heap(l, i, n):   # i é a posição do elemento
    # Se o l[i] é menor que o maior o filhos
    filho_esq =  2 * i + 1
    filho_dir = 2 * i + 2

    # Verifica se tem algum filho (necessário verificar apenas o filho_esq)
    if filho_esq >= n: 
        return 
    
    maior_filho = filho_esq

    if filho_dir < n and l[filho_dir] > l[filho_esq]:
        maior_filho = filho_dir

    if l[i] < l[maior_filho]: 
        l[i], l[maior_filho] = l[maior_filho], l[i]
        desce_heap(l, maior_filho, n)

def heap_sort(l):
    # n é tamanho do heap que atualiza conforme o maior elemento é extraído 
    n = len(l)
    for i in range(int(n/2), -1, -1): 
        desce_heap(l, i, n)

    for i in range(len(l)-1, 0, -1):
        l[0], l[i] = l[i], l[0]
        n = n - 1
        desce_heap(l, 0, n)

if __name__ == "__main__":
    l = [81, 99, 10, 11, 7, 71]
    heap_sort(l)
    print(l)
