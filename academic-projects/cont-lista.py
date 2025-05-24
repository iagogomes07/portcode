cont = []
while True:
  a = int(input('Insira um numero ou [-1] para sair: '))
  if a == -1:
    break
  cont.append(a)#retorna a uma lista especifica

print(f'{len(cont)} numeros foram digitados')#retorna o numero de elementos de uma lista