# string = 'nandao'
# mudando_str = f'{string[:3]}POW{string[4:]}'
# print(string)
# print(mudando_str)

nome = 'Fernanda Dantas'
#tam_nome = len(nome)
a = 0
novo_nome = '*'

while a < len(nome):
    novo_nome += nome[a]
    #letra = nome[a]
    #novo_nome += f'{letra}*}
    novo_nome += '*'
    a += 1

print(novo_nome)

# ou entao
texto = 'Boa noite'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
print(novo_texto)