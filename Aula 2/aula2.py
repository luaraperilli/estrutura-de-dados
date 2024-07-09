def soma(lista, n):
    soma = 0                        # Demora C1 segundos para ser executada 
    for i in range(0, n, 1):        # Demora C2 * N vezes para ser executada
        soma = soma + lista[i]      # Demora C3 * N vezes para ser executada
    return soma                     # Demora C4 segundos para ser executada 

# N = Tamanho
# Tempo total: C1 + NC2 + NC3 + C4 -> N (C2 + C3) + C1 + C4
# Constantes menores podem ser ignoradas (mantém apenas o N)
# Complexidade do Algoritmo = O(N)
# O = Ordem 
# Calcula quantas operações a função vai fazer no pior caso

l = [2, 3, 5, 7, 11, 13]
print(soma(l, 6))

def procura(lista, elemento):
    n = len(lista)                  # C1 
    for i in range(0, n, 1):        # C2 * N
        if lista[i] == elemento:    # C3 * N
            return True             # C4
    return False                    # C5

# Complexidade do Algoritmo = O(N)
print("\nTem 7 na lista: " + str(procura(l, 7)))
print("Tem 8 na lista: " + str(procura(l, 8)))

def procura2(listaA, listaB, elemento):
    for i in listaA: 
        if i == elemento:
            return True
    for i in listaB:
        if i == elemento:
            return True
    return False

lb = [2, 4, 6, 8, 10, 12]
print("\nTem 8 na lista: " + str(procura2(l, lb, 8)))
print("Tem 9 na lista: " + str(procura2(l, lb, 9))) 

def procura_comum(listaA, listaB):
    for i in listaA:                # N vezes
        for j in listaB:            # N² vezes
            if i == j:              # N² vezes
                return True
    return False

# Complexidade do Algoritmo = O(N²)
print("\nTem elemento em comum: " + str(procura_comum(l, lb)))

def procura_duplicado(listaA):
    n = len(listaA)                                 # O(1)
    for i in range(0, n, 1):                        # Vou de 0 até N portanto N vezes
        for j in range(0, n, 1):                    # N * N = N²
            if i != j and listaA[i] == listaA[j]:   # N * N = N²
                return True                         # O(1)
    return False                                    # O(1)

# i é o índice da lista
# Quando tem um for dentro do outro provavelmente é O(N²) 
# Considera-se o N de maior ordem (ignorando a constante)
# N² + N² + N = 2N² = N²
# Complexidade do Algoritmo = O(N²)

lc = [1, 2, 3, 2]
print("\nTem elemento duplicado: " + str(procura_duplicado(l)))
print("Tem elemento duplicado: " + str(procura_duplicado(lc)))
