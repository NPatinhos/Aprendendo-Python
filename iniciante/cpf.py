import random

digito = 0
contagem_regressiva_1 = 10
resultado_digito_1 = 0
nove_digitos = ''

for i in range (9):
    nove_digitos += str(random.randint(0, 9))


for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contagem_regressiva_1

digito_1 = (resultado_digito_1 % 11)

digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

contagem_regressiva_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contagem_regressiva_2

digito_2 = (resultado_digito_2 % 11)

digito_2 = digito_2 if digito_2 <= 9 else 0

cpf = nove_digitos + str(digito_1) + str(digito_2)

cpf_pontuado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:12]
print(cpf, cpf_pontuado, sep='\n')


# if cpf_calculado == cpf_usuario:
#     print('CPF valido')
# else:
#     print('CPF invalido')

