lista_compras = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir \t[a]pagar \t[l]istar \t[s]air\n')
    print()

    if len(opcao) > 2:
        print('Selecione uma opção válida\n')
        continue
    
    if opcao == 's' or opcao == 'S':
        break

    elif opcao == 'i' or opcao == 'I':
        adicionou = input('O que quer adicionar?: ')
        if adicionou == '':
            print('Adicione algum produto válido\n')
            continue
        else:
            lista_compras.append(adicionou)
    
    elif opcao  == 'a' or opcao == 'A':
        if len(lista_compras) == 0:
            print('Não há elementos para apagar')
            continue
        else:
            print('Selecione o índice do ítem a ser apagado:')
            for item in enumerate(lista_compras):
                indice, nome = item
                print(f'{indice}) {nome}')
            apagou = input('Apagar: ')

            try:
                int(apagou)
            except:
                print('Digite um valor apropriado\n')
                continue
            
            if int(apagou) < 0 or int(apagou) > indice:
                print('Não pode apagar')
            else:
                del lista_compras[int(apagou)]
                print('Apagado\n')

    elif opcao == 'l' or opcao == 'L':
        if len(lista_compras) == 0:
            print('Não há elementos na lista')
            continue
        else:
            for item in enumerate(lista_compras):
                indice, nome = item
                print(f'{indice}) {nome}')