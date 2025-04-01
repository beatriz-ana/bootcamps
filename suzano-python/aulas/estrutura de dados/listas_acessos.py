frutas = ["maçã", "laranja", "uva", "pera"]
#Acesso direto
print(frutas[0])  # maçã
print(frutas[2])  # uva

#Indices negativos
print(frutas[-1])  # pera
print(frutas[-3])  # laranja

#Matrizes
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

#Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"] - pos2 `è o inicio
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"] = pula de 2 em 2
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]