a = float(input("Insira o valor da compra: "))
b = float(input("Insira o valor da venda: "))
c = b - a
if c<0:
    d = c * -1
    print(f'O prejuizo foi de {d} reais')
elif c==0:
    print(f'Não obteve nem lucro e nem prejuizo')
else :
    print(f'O lucro foi de {c} reais')