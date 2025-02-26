#Aula sobre string - Métodos

curso = "    pYtHon  "
#Maiusculas, minusculas e título
print(curso.upper())  

print(curso.lower())

print(curso.title())

#Cortando os espaços em branco
print(curso.strip())#Remove espaços da esquerda e direita

print(curso.lstrip())#Remove espaços da esquerda

print(curso.rstrip())#Remove espaços da direita

#Junção e centralizações
menu = "Cardápio"

print(menu.center(20))
print(menu.center(20,"*"))

print("*".join(menu))


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)