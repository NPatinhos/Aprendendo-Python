#funçao q duplica, triplica e quadriplica o numero recebido

# def duplica(numero):
#     return 2*float(numero)
# def triplica(numero):
#     return 3*float(numero)
# def quadruplica(numero):
#     return 4*float(numero)

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(8))
print(triplicar(8))
print(quadruplicar(8))