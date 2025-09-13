# while   Repete um bloco enquanto a condição for verdadeira

# while condição (Sintaxe):
#     # bloco de código

qtd_repeticoes = 100
contador = 0

while contador < qtd_repeticoes:
    print(contador)
    contador = contador + 1

    if contador == 50:
        print("Parei a execucao")
        break

print("Codigo finalizado")