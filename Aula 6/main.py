import hashtable as ht
import binarytree as bt

tabela = ht.HashTable(10)

# Valores
tabela['joao'] = 4
tabela["ad"] = 3
tabela["ga"] = 5

# Chaves
print(tabela['joao'])
print(tabela['ad'])
print(tabela['ga'])

print(tabela.get("joao"))
print(tabela.get("ad"))

