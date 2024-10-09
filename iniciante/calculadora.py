def verificacao(a,b):
    try: 
        float(a)
        float(b)
    except:
        print('Digite numeros validos')
        exit()

# MAIN

print('\nBem vinda à calculadora!')

while True:

    escolha = input('\nO que você quer calcular? \n1) Adição \t\t2) Subtração \
                 \n3) Multiplicação \t4) Divisão \n5) Módulo \t\t6) SAIR\n')
    
    if escolha == '6': break
    
    a = input('numero 1:   ')
    b = input('numero 2:   ')
    verificacao(a,b)
    match escolha:
                    
            case '1':
                    print(float(a)+float(b))

            case '2':
                    print(float(a)-float(b))

            case '3':
                    print(float(a)*float(b))

            case '4':
                    print(float(a)/float(b))

            case '5':
                    print(float(a)%float(b))

            case default: 
                    print('Digite uma operação apropriada')