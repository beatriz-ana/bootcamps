#Aula sobre string - Interpolação de variaveis

nome = "Ana"
idade = 22

dados = {"nome": "Ana", "idade":22}

#Não é usado
print("Olá, me chamo %s. Eu tenho %d anos de idade." % (nome, idade))

print("\nOlá, me chamo {}. Eu tenho {} anos de idade.".format(nome, idade))

print("\nOlá, me chamo {nome}. Eu tenho {idade} anos de idade.".format(**dados))

#usado: f-string
print(f"\nOlá, me chamo {nome}. Eu tenho {idade} anos de idade.")

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")
