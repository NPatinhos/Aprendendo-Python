#input('digite oq quiser, seu dado nao é coletado: ')
#nome = input('agora coleto dado, qual seu nome? ')
#print(f'seu nome é {nome}')

valor1 = input("Digite um numero: ")
valor2 = input("DIgite outro numero: ")

try: 
    valor1 = float(valor1)
    valor2 = float(valor2)
    if valor1 > valor2: print(f'{valor1} é maior do que {valor2}')
    elif valor1 < valor2 : print(f'{valor2} é maior do que {valor1}')
    else: print(f'{valor1} é igual a {valor2}')

except:
    print(f'Digita números animal')

# if float(valor1) == True or float(valor2) == True: 
#     if float(valor1) > float(valor2): print(f'{valor1} é maior do que {valor2}')
#     elif float(valor1) < float(valor2): print(f'{valor2} é maior do que {valor1}')
# #elif float(valor1) == float(valor2): print(f'{valoar1} é igual a {valor2}')
#     else: print(f'{valor1} é igual a {valor2}')
    
# else:print('Digita numeros válidos animal')

    