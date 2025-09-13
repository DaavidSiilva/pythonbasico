#Um dicionário é como uma caixa com etiquetas. 
#Em vez de guardar valores em posições (como nas listas e tuplas)
#Você guarda cada valor com um nome (chave).

# keys/values/items

#Sintaxe:
# nome_do_dicionario = {
#       chave:valor,
#       chave:valor,
#       chave:valor     
#                      }

carro = {
    "ano":1994,
    "modelo": "gol",
    "montadora": "volks"
}

#print(type(carro))
print(f"O ano do carro e {carro["ano"]}")
print(f"O modelo do carro e {carro["modelo"]}")

#Chaves
print("------------------------------------")
print(f"As chaves do dict sao: {carro.keys()}")

#Valores
print("------------------------------------")
print(f"Os valores do dict sao: {carro.values()}")

#Itens
print("------------------------------------")
print(f"Os items do dict sao: {carro.items()}")

#Laco
print("------------------------------------")
for chave, valor in carro.items():
    print(f"A Chave: {chave} possui o valor: {valor}")

#Adicionando Chave
carro["placa"] = "DVD-1453"

#Pesquisar Valores/Chaves
print("------------------------------------")
if "placa" in carro:
    print(f"A Placa do veiculo e: {carro["placa"]}")
else:
    print(f"Placa nao cadastrada")

print("------------------------------------")
del carro["placa"]
print(carro)