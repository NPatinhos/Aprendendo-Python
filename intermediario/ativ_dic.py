# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
certas = 0

for pergunta in perguntas:
    print('\n', 'Pergunta:', pergunta['Pergunta'])

    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao} ')

    palpite = input('Escolha uma opção: ')
    try:
        int(palpite)
    except TypeError as error:
            print('Errado')

    palpite_resposta = pergunta['Opções'][int(palpite)]
    if palpite_resposta == pergunta['Resposta']:
        print('Certo')
        certas+=1
    else:
         print('Errado')

print(f'\nVocê acertou {certas} de {len(perguntas)} perguntas!\n')