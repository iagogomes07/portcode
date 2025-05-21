def consciente (a):
  if a > 0:
    return print('valor positivo')
  elif a == 0:
    return print('valor nulo')
  else:
    return print('valor negativo')
  
a = float(input('Digite um valor:'))
consciente(a)