#Tuplas são coleções/Listas imutáveis.

numeros = (1,2,3,4,5)                   #Tupla
numeros_lista = [1,2,3,4,5]             #Lista
#print(type(numeros))

print(f"A primeira posicao da tupla possui o valor {numeros[0]}")

print("-----------------------------------")
for idx, valor in enumerate(numeros):
    print(f"A Posicao {idx}, possui o valor {valor}")

print("-----------------------------------")
#Pesquisar Valor em Tuplas
print(f"O numero 1 aparece {numeros.count(1)} vez(es)")

#Indice Baseado em Valor
print("-----------------------------------")
print(f"O numero 1 esta na posicao {numeros_lista.index(4,0)} ")

print("-----------------------------------")
#Pesquisando valores em lista
print(f"O numero 1 esta na lista numeros_lista?\n{1 in numeros_lista}")
print(f"O valor 2 esta no indice: {numeros_lista.index(2)}")

print("-----------------------------------")
#Contando posicoes
#Lista
print(f"A Lista possui {len(numeros_lista)} posicoes.")

#Tupla
print(f"A Tupla possui {len(numeros)} posicoes.")