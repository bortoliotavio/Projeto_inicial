#Desafio

nome = input("Digite o seu nome: ")
salario = float(input("Digite seu salario: "))
bonus = float(input("Digite a porcentagem da sua bonificação: "))
bonus = 1000 + salario * bonus

print(f"Olá {nome}, o seu bônus foi de {bonus}")