#Programa de Calculo de Area - Try ; Except

try:
    medida = float(input("Digite a Medida: "))
    area = medida * medida
    print(f"A area total é de: {area}")
except Exception as erro:
    print(f"O valor digitado é invalido, Erro: {erro}")
finally:
    print("Codigo finalizado")