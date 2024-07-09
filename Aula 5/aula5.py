# Conflitos: quando duas ou mais chaves são mapeadas para a mesma posição da tabela
# Outro método de resolução dos conflitos (além de lista encadeada) é a sondagem linear
# Quando ocorre uma colisão a sondagem linear tenta resolver o problema movendo-se para a próxima posição disponível na tabela até encontrar uma posição vazia
# Exemplo: em uma tabela hash com sondagem linear as posições 5, 6, 7 e 8 já estão ocupadas. Se você tentar inserir um novo elemento e ele colidir na posição 5, a sondagem linear verificará a próxima posição (6) e descobrirá que está ocupada. Em seguida, verificará a posição 7, que também está ocupada, e assim por diante até encontrar um slot vazio. Se houver várias colisões consecutivas, elas formarão um cluster

class HashItem:
    def __init__(self, key, value):
        self.key = key  # Chave
        self.value = value  # Valor

class HashTable:
    def __init__(self, size):   # Construtor
        self.size = size
        self.slots = [None for i in range(size)]    # De 0 até size variando de 1 em 1. Criação de uma lista com o valor None para todas as posições de i até o tamanho da lista
        self.count = 0  # Contador

    def _hash(self, key):   # Função que começa com _ é private (utilizar apenas dentro da própria classe)
        count = 1
        value = 0
        for c in key: 
            value = value + (ord(c) * count)
            count += 1
        return value % self.size    # Deve me retornar um valor entre 0 até o tamanho da tabela
    
    def put(self, key, value):
        item = HashItem(key, value) # Item que quero colocar na tabela hash
        hashValue = self._hash(key) # Me devolve o valor de hash daquele item, ou seja, onde vou colocá-la na tabela (não insere na tabela ainda)
        position = hashValue
        # Enquanto a posição for diferente de None soma 1 até encontrar um espaço vazio para inseri-lo
        while self.slots[position] != None:
            if self.slots[position].key == key:
                break   # Se a chave já existe vamos atualizar o valor
            position = (position + 1) % self.size
        # Colocar ou atualizar na posição position
        if self.slots[position] == None:
            self.count += 1
            self.check_growth()
        self.slots[position] = item # Insere o item na posição disponível encontrada

    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor >= 0.75:   # Quando a tabela for 75% ocupada seu tamanho é dobrado
            self.growth()

    def get(self,key):  # Fazer busca
        hashValue = self._hash(key) # Pega o hashValue daquela chave
        position = hashValue    # Variável usada para percorrer a tabela hash enquanto procura pela chave
        while self.slots[position] != None: # Verifica se o valor não é None antes de percorrer
            if self.slots[position].key == key: # Verifica se a chave na posição atual position é igual à chave buscada
                return self.slots[position]. value
            position = position + 1 % self.size # Se a chave na posição atual não for a chave procurada incrementa-se position em 1
        return None # Se acabar o while sem encontrar a chave ela não está presente na tabela

    def growth(self):   # Dobrar o tamanho da tabela hash 
        print("Cresceu")
        new_size = 2 * self.size
        new_table = HashTable(new_size)
        # Traz os elementos da tabela antiga para a nova
        for i in range(self.size):
            if self.slots[i] != None:
                new_table.put(self.slots[i].key, self.slots[i].value)
        self.size = new_size    # Atualiza o tamanho da tabela
        self.slots = new_table.slots[:]

if __name__ == "__main__":

    Tabela = HashTable(10)
    Tabela.put('joao', 5)
    Tabela.put('ad', 6)
    Tabela.put('ga', 3)

    Tabela.put('python', 10)
    Tabela.put('code', 7)
    Tabela.put('programming', 8)
    Tabela.put('data', 4)
    Tabela.put('structure', 9)
    Tabela.put('algorithm', 6)
    Tabela.put('hash', 2)   

    for i in range(10):
        if Tabela.slots[i] != None:
            print(Tabela.slots[i].key, Tabela.slots[i].value)
        else:
            print('Vazio')

    print(Tabela.slots)




