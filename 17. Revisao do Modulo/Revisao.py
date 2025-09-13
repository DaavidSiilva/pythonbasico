#Crie um programa que receba os dados de uma pessoa (Altura, Peso) e calcule o IMC.  (04. Input/Output)
#Formula para o IMC: peso / (altura ** 2)                                            (05. Operadores Matematicos)
#Baseado no resultado, exiba na tela a classificacao baseado em:                     (07. Desvio Condicional)

    # IMC < 18.5: "Abaixo do peso"
    # IMC <   25: "Peso normal"
    # IMC <   30: "Sobrepeso"
    # Senao:      "Obesidade"

#Altura
while True:
    try:
        altura = float(input("Digite sua altura: "))
        break   
    except:
        print("Digite um valor valido!")

#Peso
while True:
    try:
        peso = float(input("Digite sua peso: "))
        break   
    except:
        print("Digite um valor valido!")

imc = round(peso / (altura ** 2),2)                #altura * altura

if imc < 18.5:
    print(f"IMC: {imc}, Classificacao: Abaixo do Peso")
elif imc < 25:
    print(f"IMC: {imc}, Classificacao: Peso Normal")
elif imc < 30:
    print(f"IMC: {imc}, Classificacao: Sobrepeso")
else:
    print(f"IMC: {imc}, Classificacao: Obesidade")