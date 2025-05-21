def modulo (a):
    if a >= 0:
        return a
    else:
        return (a * -1)
    
a = float(input('Digite um valor:'))
r = modulo(a)
print(f'O modulo de {a} é {r}')