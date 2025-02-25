#Aula sobre estruturas de repetição - BREAK

'''while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)'''

for numero in range(100):

    if numero % 2 == 0: #numero par e só imprime impares
        continue

    print(numero, end=" ")