n = []
while True:
  a = float(input('Insira uma nota ou [-1] para sair: '))
  if a == -1:
    break
  n.append(a)

if n:
  me = sum(n) / len(n) #sum soma 
  print(f'A média de {len(n)} alunos foi {me}')