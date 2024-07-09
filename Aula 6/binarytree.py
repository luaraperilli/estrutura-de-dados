# Binary Tree
# Possui chave, valor, filho esquerdo e filho direito
# Chaves à direita são menores
# Chaves à esquerda são maiores

class BinaryTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    # Função para inserir elementos na árvore
    def put(self, key, value):
        # Verificar se a chave do nó atual é igual à chave que está sendo inserida. Se sim, atualiza o valor do nó com o novo valor
        if self.key == key:
            self.value = value
        # Verifica se a chave sendo inserida é menor que a chave do nó atual
        # Se a chave for menor, verifica se o nó left é nulo. Se sim, cria um novo nó com a chave e valor fornecidos
        # Se não, chama o método put para continuar a inserção na subárvore à esquerda
        if self.key > key:
            if self.left == None:
                self.left = BinaryTree(key, value)  
            else:
                self.left.put(key, value)
        # Verifica se a chave sendo inserida é maior que a chave do nó atual
        # Se sim, verifica se o nó à direita é nulo. Então cria um novo nó à direita com o chave e valor fornecido
        # Se não for nulo, já existe um valor à direita desse nó. Então, insere na subárvore à ireita
        if self.key < key:
            if self.right == None:
                self.right = BinaryTree(key, value)
            else: 
                self.right.put(key, value)
        return
    
    def print(self):
        print("(", end='')
        if self.left != None:
            self.left.print()
        print(str(self.key) + " " + str(self.value), end='')
        if self.right != None:
            self.right.print()
            print(")", end='')

    def get(self, key):
        if self.key == key:
            return self.value
        if key < self.key:
            if self.left == None:
                return None
            else: 
                return self.left.get(key)
        if key > self.key:
            if self.ritht == None:
                return None
            else: 
                return self.right.get(key)

# if __name__ == "__main__":
#     BT = BinaryTree('joao', 3)
#     BT.put('ad', 4)
#     BT.put('ga', 2)
#     BT.put('Joaa', 4)
#     BT.print()