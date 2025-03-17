def fora(x):
    a = x
    b = x

    def dentro():
        nonlocal b
# se nao usar nonlocal, tentar *mudar* a variavel b da erro pq seu valo foi definido antes,
# mas pode *criar* um novo valor p ela
        b += 1
        return b
    return dentro

dentro = fora(6)
print(dentro())
print(dentro)