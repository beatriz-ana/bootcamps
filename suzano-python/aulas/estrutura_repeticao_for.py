#Aula sobre estruturas de repetição - FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executo no final do laço")


# exibindo a tabuada do 5
for numero in range(0, 51, 5):# começo, start , step(vai de 5 em 5)
    print(numero, end=" ")
