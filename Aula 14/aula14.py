# Árvore Rubro-Negra (esquerdista)
# Left leaning
# Árvore binária de busca balanceada
# Nós podem ser vermelhos ou pretos
# Os nós à esquerda têm valores menores e todos os nós à direita têm valores maiores
# As folhas da árvore são consideradas pretas e None (ausência de valor)
# Se um nó é vermelho ambos os seus filhos são pretos
# Se um nó é vermelho ele é filho esquerdo do pai
# Raíz é preta
# Altura Negra: para cada nó x o número de nós PRETOS é o mesmo para qualquer folha descendente (não considerar o próprio x nem os nós vermelhos)

# A nova raíz herda a cor do pai no balanceamento:
# 7 é vermelho
#        (5)
# (Alfa)      (7)
#        (Beta) (Gama)

# Após baçanceamento:
# 5 é vermelho
#           (7)
#      (5)      (Alfa)
# (Gama) (Beta)

class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.cor = True  # Se for True é vermelho

# Rotaciona a esquerda e devolve o novo nó pai
def rotaciona_esquerda(no_y):    # no_y é a raíz de uma sub árvore
    no_x = no_y.dir
    no_y.dir = no_x.esq
    no_x.esq = no_y
    no_x.cor = no_y.cor
    no_y.cor = True
    return no_x

# Rotaciona a direita e devolve o novo nó pai
def rotaciona_direita(no_y):      # no_y é a raíz de uma sub árvore
    no_x = no_y.esq
    no_y.esq = no_x.dir
    no_x.dir = no_y
    no_x.cor = no_y.cor
    no_y.cor = True
    return no_x

# Verifica se o nó é vermelho
def eh_vermelho(N):
    return N is not None and N.cor

# Verifica se o nó é preto
def eh_preto(N):
    return N is None or not N.cor

# Sobem o vermelho do nó e seus filhos
def sobe_vermelho(no_y):
    no_y.cor = True
    no_y.esq.cor = False
    no_y.dir.cor = False

# Insere um novo nó na árvore
def insere_aux(raiz, dado):       # Recebe uma árvore e devolve uma nova árvore com o dado adicionado
    if raiz is None:
        return No(dado)
    if dado < raiz.dado: 
        raiz.esq = insere_aux(raiz.esq, dado)
    elif dado > raiz.dado:
        raiz.dir = insere_aux(raiz.dir, dado)
    # Conserta a árvore:
    if eh_vermelho(raiz.dir) and eh_preto(raiz.esq):
        raiz = rotaciona_esquerda(raiz)
    if eh_vermelho(raiz.esq) and eh_vermelho(raiz.esq.esq):
        raiz = rotaciona_direita(raiz)
    if eh_vermelho(raiz.esq) and eh_vermelho(raiz.dir):
        sobe_vermelho(raiz)
    return raiz

# Função principal de inserção
def insere(raiz, dado):
    raiz = insere_aux(raiz, dado)
    raiz.cor = False
    return raiz

# Imprime a árvore
def imprime(raiz):
    if raiz is None:
        return
    print("(", end="")
    imprime(raiz.esq)
    cor = "V" if raiz.cor else "P"  # V para vermelho e P para preto
    print(" , " + str(raiz.dado) + cor + " , ", end="")
    imprime(raiz.dir)
    print(")", end="")

if __name__ == "__main__":
    raiz = None
    raiz = insere(raiz, 5)
    imprime(raiz)
    print()
    raiz = insere(raiz, 7)
    imprime(raiz)
    print()
    raiz = insere(raiz, 3)
    imprime(raiz)
    print()
    raiz = insere(raiz, 4)
    imprime(raiz)
    print()
    raiz = insere(raiz, 6)
    imprime(raiz)
    print()


