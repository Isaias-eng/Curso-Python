'''
Tipo de tipagem do python = Dinânimca / forte
str - string - texto
Strings são textos que esyão sempre dentro de aspas ""/''

'''

print("Isaias \"Sampaio") # \ = caractere de escape
print(r"Isaias \"Sampaio")

'''
Tipos int e float
int = número inteiro positivo ou negativo
'''
print(20) # int
print(-10) # int
print (0) # int

'''
float = número com ponto flutuante positivo ou negativo
'''
print(1.9, 2.0) # float

# A função type() mostra o tipo que o python inferiu ao valor
print(type('Isaias')) # str
print(type(2005)) # int
print(type(1.0), type(-2.0), type(4))

'''
Bool(boolean) = dado que só tem dois valores True ou False
Existem vários operadores para "questionar"
Dentre eles o ==, é um operador lógico que questiona se um valor é igual a outro
'''
print(10 == 10) # True
print(10 == 12) # False
print(type(10 == 10)) # bool
