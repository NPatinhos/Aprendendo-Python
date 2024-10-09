palava_secreta = 'cadeado'
descoberto = ''
adivinhando = ''
i = 0
tentativas = 0

#forma palavra criptografada
for a in range(len(palava_secreta)):
    adivinhando += '*'
    a+=1

while True:
#verificando se o caractere é valido
    chute = input('Digite uma letra: ')
    if len(chute) > 1:
        print('Digite só 1 letra\n')
        continue
    elif chute == '' or chute == ' ':
        continue

#loop para dar o valor de cada index a letra acertada
    while i < len(palava_secreta):
#        p =palava_secreta[i]
        if chute == palava_secreta[i]:
            descoberto = f'{adivinhando[:i:]}{chute}{adivinhando[i+1::]}'
            adivinhando = descoberto
        i+=1
#nao acertou a letra
    if chute not in palava_secreta:
        print('Tente novamente\n')    
    print(adivinhando)
    print()
    i = 0
    tentativas+=1
#quando acertar acaba o loop
    if adivinhando == palava_secreta: 
        break
    else:
        continue

print(f'Parabens! A palavra é "{palava_secreta}" \nVocê conseguiu em {tentativas} tentativas\n')


#  JEITO MAIS FACIL
'''
if chute in palavra_secreta:
    adivinhando += chute

descoberto = ''
for letra_secreta in palavra_secreta:
    if letra_secreta in adivinhando:
        descoberto += letra_secreta
    else: adivinhando += '*'







'''
