#Aula sobre Funções - Objetos de primeira classe

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

op = somar

print(op(2,5))
exibir_resultado(10, 10, somar)

