# Listas em Python
# Insert / Pop
# Sort() / Reverse()

numeros = [1,2,3,4,5]
print(f"A primeira posicao tem o valor: {numeros[0]}")

numeros.insert(0,0)
print(f"A primeira posicao tem o valor: {numeros[0]}")

numeros.pop(0)
print(f"A primeira posicao tem o valor: {numeros[0]}")

#Primeiro Laco
print("--------------------------------")
for numero in numeros:
    print(f"O Numero atual e: {numero}")

print("--------------------------------")
for indice, valor in enumerate(numeros):
    print(f"A posicao: {indice} tem o valor: {valor}")

#Sort/Reverse
print("--------------------------------")
numeros.reverse()
for indice, valor in enumerate(numeros):
    print(f"A posicao: {indice} tem o valor: {valor}")

print("--------------------------------")
lista_exemplo = ["David", 34, 1.78, True]
print(type(lista_exemplo[3]))
