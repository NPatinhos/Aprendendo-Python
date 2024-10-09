nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]
letras = len(nome)
primeira = nome[:1:]
# primeira:   nome[0]
ultima = nome[-1::]
# ultima:  nome[-1]

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome: print('Seu nome contém espaços')
    else: print('Seu nome não contém espaços')
    print(f'Seu nome tem {letras} letras')
#   print(f"seu nome tem {len(nome)} letras")
    print(f'Primeira letra: {primeira}')
    print(f'Ultima letra: {ultima}')
else: print('Voce deixou campos vazios')
