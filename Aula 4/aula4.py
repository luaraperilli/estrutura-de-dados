# Conjuntos não são ordenados e não possuem elementos repetidos
# Não é possível colocar um conjunto dentro do outro
# Objetos de um conjunto devem ser imutáveis

A = set([1, 2, 3])
print(A)

B = set([3, 4, 5])
print(A.union(B)) # Na união os elementos repetidos são eliminados
print(A|B) # Também realiza união
# União não funciona como append. Copia os elementos do conjunto anterior e cria um novo conjunto

print(A.intersection(B)) # Mostra os elementos que estão em ambos os conjuntos
print(A & B) # Também realiza interseção

print(A.symmetric_difference(B)) # Diferença simétrica é a união dos conjuntos exceto os elementos iguais
print(A ^ B) # Também realiza diferença simétrica

print(A.issubset(B))
C = set([1, 2, 3, 4, 5])
print(A.issubset(C))

A = set([1, 'String', (1, 2)])
print(A)

X = 4500
A = set(range(0, X, 1))
for i in range (X, X+10, 1):
    # A = A.union(set([i])) Ineficiente
    A.add(i) # Mais eficiente que o Union
print(len(A))
# Considerando os conjuntos A = N e B = M
# Complexidade de Union = O(N + M)
# Complexidade do Add = O(1)

# Comando frozenset faz os conjuntos serem imutáveis e, assim, é possível unir conjuntos (não é mais possível adicionar elementos)
X1 = frozenset(['Luara'])
X2 = frozenset(['Dados'])
X3 = frozenset([10])
XX = {X1, X2, X3}
print(XX)

# Tabela Hash
print(ord('L')) # Para cada caractere retorna um número de 0 até 256
endereco = ord('L') + ord('u') + (ord('a')) + (ord('r')) + (ord('a'))
print(endereco)
# Map faz o mesmo que a linha 48
print(sum(map(ord, 'Luara')))
# O mesmo usuário/pessoa pode possuir o mesmo endereço
print(sum(map(ord, 'Laura')))
# Função para consertar o problema acima (fazendo com que a posição dos caracteres seja multiplicada pelo valor da tabela hash):
# Exemplo: João = 106 * 1 + 111 * 2 + 93 * 3 + 111 * 4
def myHash(s):
    contador = 1 
    valor = 0
    for c in s:
        valor = valor + (ord(c) * contador)
        contador += 1
    return valor 

# Testes
print(myHash('Luara'))
print(myHash('Laura'))
# Entretanto, ainda podem ocorrer colisões. Exemplo:
print(myHash('ad'))
print(myHash('ga'))
# A Sondagem Linear (Linear Probing) é um esquema em programação para resolver colisões em tabelas de hash
# O problema também pode ser solucionado por meio de Listas Encadeadas/Ligadas
# Os elementos de mesmo endereço vão para uma mesma lista e é necessário fazer uma busca linear:
# 297 = | ga | -> | ad | -> | João |
# Os elementos de mesmo endereço também podem ir para uma árvore binária 
# Dicionário também é uma tabela hash