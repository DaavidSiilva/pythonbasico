alunos = {
    "joao": {"idade": 20, "curso": "Python"},
    "maria": {"idade": 22, "curso": "JavaScript"},
    "ana": {"idade": 19, "curso": "Visual Basic"}
}

print("-" * 50)
print(f"O aluno Joao esta no curso {alunos['joao']["curso"]}")

print('Lista Original')
print(alunos)
#Exclusao
del alunos["ana"]

#Informacao original
print('Lista Modificada')
print(alunos)


print("-" * 50)
#Lacos de Repeticao
for chave, valor in alunos.items():
    print(f"A Chave e: {chave}, o Valor e: {valor}, o Curso e: {valor["curso"]}, A Idade e: {valor["idade"]}")

