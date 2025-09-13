#Baseado no dicionario disponibilizado:
#Crie um programa que calcule a media de cada aluno (05. Operadores Matematicos)
#Se a media for maior ou igual 5: Aprovado senao: Reprovado (07. Desvio Condicional)
#Crie uma lista com os alunos aprovados e uma lista com os alunos reprovados    (11. Listas)
#Exiba na tela as duas listas com o nome do aluno, o status e a media           

alunos = {
    "Joao": [7.5, 6.0, 8.0],
    "Maria": [4.0, 5.0, 3.5],
    "Carlos": [9.0, 8.5, 9.5],
    "Ana": [5.0, 5.5, 6.0],
    "Lucas": [2.5, 4.0, 3.0]
}

aprovados = []
reprovados = []

for chave, valor in alunos.items():
    
    nota1 = valor[0]
    nota2 = valor[1]
    nota3 = valor[2]

    media = round((nota1 + nota2 + nota3) / 3,2)       #Ou sum(valor)
    
    if media >= 5:
        aprovados.append([chave, media, "Aprovado"])
    else:
        reprovados.append([chave, media, "Reprovado"])

#Exibir para o Usuario
print("Alunos Aprovados:")
for aluno in aprovados:
    print(f"Nome: {aluno[0]}\nMedia: {aluno[1]}\nStatus:{aluno[2]}")
    print(50 * "-")

print("\n------------\n")

print("Alunos Reprovados:")
for aluno in reprovados:
    print(f"Nome: {aluno[0]}\nMedia: {aluno[1]}\nStatus:{aluno[2]}")
    print(50 * "-")