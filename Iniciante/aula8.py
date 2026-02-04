#Precedência entre os operadores lógicos

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

# Cálculo IMC

nome = 'Isaias'
altura = 1.60
peso = 56.5

imc = peso / altura**2

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos', 'e seu IMC é de: ', imc)

# Formatação de strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é de: {imc:.3f}'
print(linha_1)
print(linha_2)