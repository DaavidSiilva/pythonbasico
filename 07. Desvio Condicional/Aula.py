# Desvios Condicionais

# if     Executa um bloco se a condição for verdadeira
# elif   (else if) Nova condição se a anterior for falsa
# else   Executa um bloco se todas as condições anteriores forem falsas

# Exemplo de estrutura (Sintaxe):
# if condição:
#     # bloco se for verdadeiro
# elif outra_condição:
#     # outro bloco
# else:
#     # bloco final se nenhuma for verdadeira

gols_time_a = 1
gols_time_b = 2

if gols_time_a > gols_time_b:
    print("O Campeao é o Time A!")
elif gols_time_b > gols_time_a:
    print("O Campeao é o time B!")
else:
    print("Empate")