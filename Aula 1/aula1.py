# Aula 1  - Estrutura de Dados 2

# Mostra o tipo da variável
# type(x) 

# Função bool transforma qualquer coisa que não seja 0 em True
# 1 = True
# x = bool(1)

# 0 = False
# x = bool(0)

x = 'hokama'
print(x)
# Significa que x aponta para a str 'hokama'
# Se eu disser que x = imc o x passa a apontar para 'imc' mas a str 'hokama' ainda existe e é inalterável

x = 5
x = 4 
y = 4
id(x) # Mostra o endereço de memória de x (4)
id(y) # Também mostra o endereço de memória de x (4)

# Concatenar
n = 'Pedro'
s = 'Hokama'
nome = n + s
print(nome)

# Lista
# Lista pode ter tipos diferentes
A = [1, 2, 3]
B = [2, 'Hokama', 4]
C = [A, B, 1, 2, 3]
print(C)
# Operador in responde se determinado elemento está dentro de uma sequência
# 1 in C retorna True pois 1 está na lista C
# 4 in C retorna False pois 4 está na lista B apenas
# A [2] me retorna o segundo elemento da lista A

A[2] = 5 # Substitui o segundo elemento da lista A por 5 (não muda o endereço de memória, ou seja, pra onde aponta o A)
print(A)
# Se mudo a lista A também muda o que tem dentro da lista C
# A.append(12) adiciona o elemento 12 na lista A. Insere no mesmo endereço de memória e A = [10, 11, 12]
A = [10, 11] # Se fizermos A = [10, 11] ele passa a apontar para o endereço de memória [10, 11]
B = A 
B.append(13) # Se faço B = A o B passa a apontar para o mesmo endereço do A. Assim, se faço B.append(13) o A também teria o 13 inserido
C = [A, B, 1, 2, 3]
print(C)
# del(A[1]) Apaga o primeiro elemento da lista

# Range = (valor inicial, valor final e o passo). Exemplo: de 1 até 10 pulando de 1 em 1
range(1, 10, 1)
2 in range(1, 10, 1) # Retorna True pois 2 está dentro do range
2 in range(1, 10, 2) # Retorna False pois 2 não está dentro do range
# Range não é uma lista e sim uma sequência
# A[:-2] Mostra todos os elementos de A exceto os dois últimos

len(A) # Mostra o tamanho da lista
min(A) # Mostra o menor número de A
max(A) # Mostra o maior número de A

A = [1, 2]
A = A + [3] # Cria um novo endereço com [1, 2, 3] e perde-se o [1, 2] anterior
print(A)

B = [1, 2]
B.append(3) # Coloca o 3 no mesmo endereço de [1, 2]
B