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

# certas = 0
# def checar_resposta(palpite, pergunta['Resposta']):
#     if palpite == pergunta['Resposta']:
#         certas+=1
#         print('Acertou')
#     else:
#         print('Errou')

for pergunta in perguntas:
    print('\n', 'Pergunta:', pergunta.get('Pergunta'))
    for item in enumerate(pergunta['Opções']):
        indice, opcao = item 
        print(f'{indice}) {opcao} ')
    palpite = input('Escolha uma opção: ')
    try:
        int(palpite)
    except:
        FileNotFoundError
    if palpite == 'Opções'[palpite]:
        print('certo')




# ESSE METODO É ANTIGO, TEM Q FAZER COM AS FUNÇOES DE DICIONARIO keys() e values()
# for questao in perguntas:
#     print('\n', questao['Pergunta'])
#     for item in enumerate(questao['Opções']):
#         indice, opcao = item 
#         print(f'{indice}) {opcao} ')

    
