# Print: Exibe um texto ou valor no terminal;tela
# Input: Captura um texto ou informacao do usuario

#print("Nome do usuario é: David Silva")
nome_usuario = input("Digite o seu nome: ")
idade = 34
altura = 1.78
nacionalidade = "Brasileiro"

#print("Nome do usuario é: " + nome_usuario)
#print(f"Nome do usuario é: {nome_usuario}\nIdade: {str(idade)}\nAltura: {str(altura)}\nNacionalidade: {nacionalidade}")
print("Nome do usuario é: {}\nIdade: {}\nAltura:{}".format(nome_usuario,idade, altura))