def fat(a):
    r = 1
    for i in range(1, a + 1):
        r =  r * i
    return r
    
a = int(input('insira um valor inteiro:'))
r = fat(a)

if a > 0: 
    print (f'{a}! = {r}')
elif a == 0:
    print (f'{a}! = 1')  
else:
    print ('fatorial de numero negativo n existe')