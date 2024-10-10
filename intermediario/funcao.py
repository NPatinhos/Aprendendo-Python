def multiplica(*args):
    produtorio = 1
    for valor in args:
        produtorio *= valor

    return produtorio

print(multiplica(1, 5, 7, 3))

def parouimpar(a):
    if a % 2 == 0:
        return 'É par'
    else:
        return 'É impar'
    
print(parouimpar(multiplica(1, 5, 7, 3)))