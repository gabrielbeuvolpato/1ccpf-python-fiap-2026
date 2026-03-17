print("Ola mundo")

print(7 + 4)
print("7 + 4")
print("7" + "4") #CONCATENAÇAO DE STRINGS

#variavel

nome ="Gabriel"
idade = 18
peso = 72

print(nome, idade, peso)
print(f"Ola,{nome}")

#input
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso: "))

print(nome, idade, peso)

#desafio 1

nome1 = input("Digite seu nome: ")

print(f"Ola,boa vindas,{nome1}")

#desafio 2

dia = int(input("Digite o dia que voce nasceu: "))
mes = int(input("Digite o mes que voce nasceu: "))
ano = int(input("Digite o ano que voce nasceu: "))

print(f"Voce nasceu na data {dia}/{mes}/{ano}")

#desafio 3

n1 = int(input("Digite o primeiro numero que deseja somar: "))
n2 = int(input("Digite o segundo numero que deseja somar: "))

soma = n1 + n2

print(f"A soma foi um total de {soma}")