# Listas em Python: Bidimensionais

alunos = [	
	["David", 34, 1.78, True],
	["Ana", 36, 1.65, True],
	["Leandro", 40, 1.80, True]
]

#print(f"A posicao 0 possui a lista {alunos[0]}")
#print(f"O nome do primeiro aluno da lista alunos e: {alunos[0][0]}, sua idade e: {alunos[0][1]}")

for indice, aluno in enumerate(alunos):
    print(f"O Aluno {indice}:")
    print(f"Nome: {aluno[0]}\nIdade: {aluno[1]}\nAltura: {aluno[2]}\nNacionalidade: {aluno[3]}")
    print("--------------------------------------------")