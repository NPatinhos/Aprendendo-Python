# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

print('----------- PRIMEIRO EXERCICIO ----------------\n\n')
num_int = input('Digite um inteiro: ')

try:
    int(num_int)
    num_int.isdigit
    e_par = (int(num_int) % 2)

    if not e_par: print('O número é par') 
    else: print('O número é ímpar') 

except:
    print('Não é inteiro')

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
print('\n\n----------- SEGUNDO EXERCICIO ----------------\n\n')

hora = input('Que horas são: ')
try:
    hora.isdigit
    if int(hora) >= 0 and int(hora) <= 11: print('Bom dia!')
    elif int(hora) >= 12 and int(hora) <= 17: print('Boa tarde!')
    elif int(hora) >= 18 and int(hora) <= 23: print('Boa noite!')
    else: print('Digite um horario apropriado')


except:
    print('Digite um horario apropriado')



# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

print('\n\n----------- TERCEIRO EXERCICIO ----------------\n\n')

nome = input('Digite seu nome: ')

if len(nome) <= 4: 
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6: 
    print('Seu nome é normal')
else: print('Seu nome é enorme')