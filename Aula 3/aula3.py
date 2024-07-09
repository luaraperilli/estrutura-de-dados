import math

def busca (lista, elemento):
    tamanho = len(lista)
    for i in range (0, tamanho, 1):
        if lista [i] == elemento:
            return True
    return False

# Busca Binária: parte do pressuposto de que o vetor está ordenado e realiza divisões do espaço de busca comparando o elemento buscado (chave) com o elemento no meio do vetor. 
# Se o elemento do meio do vetor for a chave, a busca termina com sucesso. 
# Se o elemento do meio vier antes do elemento buscado, então a busca continua na metade posterior do vetor.
# Se o elemento do meio vier depois da chave, a busca continua na metade anterior do vetor.

def busca_binaria (lista, elemento, posicao_inicial, posicao_final):
    if posicao_final <= posicao_inicial:
        return False
    # math.floor: se a divisão resultar em, por exemplo, 5.5, arredonda para baixo.
    meio = math.floor((posicao_final - posicao_inicial)/2) + posicao_inicial
    if lista[meio] == elemento:
        return True
    if lista[meio] > elemento:
        # Os dois últimos parâmetros são os limites da lista: do início ao meio
        return busca_binaria(lista, elemento, posicao_inicial, meio)
    if lista[meio] < elemento:
        # Do meio+1 até o final da lista
        return busca_binaria(lista, elemento, meio+1, posicao_final)
    return False

if __name__ == "__main__":
    # l = [5, 1, 20, 11, 8, 7, 9, 12]
    l = [1, 5, 7, 8, 9, 11, 12, 20]
    # A partir da posição zero e, por fim, o tamanho da lista
    print(busca_binaria(l, 11, 0, len(l)))
    print(busca_binaria(l, 20, 0, len(l)))
    print(busca_binaria(l, 1, 0, len(l)))
    print(busca_binaria(l, 13, 0, len(l)))
    print(busca_binaria(l, 6, 0, len(l)))

    # Tupla aceita qualquer tipo de objeto
    minha_tupla = ('Luara', 'IMC', 30)
    print(minha_tupla[1])
    m = minha_tupla * 2
    print(m)
    
    minha_tuplaB = ('Luara', 'IMC')
    print(id(minha_tuplaB)) # Endereço de memória
    minha_tuplaB = minha_tuplaB + ('Bloco C', 'LDC 2')
    print(minha_tuplaB)
    print(id(minha_tuplaB)) # Endereço de memória

    minha_tuplaB = minha_tuplaB + (1,)  # Tupla só aceita ter um elemento único adicionado com a vírgula
    print(minha_tuplaB)

    # Lista = []
    # Tupla = ()
    # Dicionário = {}

    professor = {
        # Chave : Valor
        'Nome' : 'Luara',
        'Instituto' : 'IMC',
        'Sala' : 6
    }
    print(professor)
    print(professor['Nome'])
    print(professor.get('Instituto'))
    print(id(professor))

    # No Dicionário é possível fazer alterações no mesmo endereço de memória
    professor['Sala'] = 2
    print(professor['Sala'])
    print(id(professor)) # Mesmo endereço de antes da alteração

    # Solicitar informações do Dicionário
    print(professor.items())
    print(professor.keys())
    print(professor.values())
    print(professor.pop('Nome')) # Remove a Chave-Valor 'Nome'
    # print(professor.popitem()) Remove o último do Dicionário

    p2 = {
        'Sala' : 'LDC5',
        'Instituto' : 'IRN'
    }

    professor.update(p2)
    print(professor)