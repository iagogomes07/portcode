alt = []
gen = []

while True:
    a = float(input("\nDigite a altura em metros ou [0 para sair]: "))
    if a == 0:
        break
    g = str(input("Gênero (m/f): ").lower())
    while g not in ['m', 'f']:
        print("Opção inválida! Digite 'm' ou 'f'")
        g = input("Gênero (m/f): ").lower() #.lower() joga tudo pra minusculo e .upper para maiusculo()
    alt.append(a)#adiociona a lista alt[]
    gen.append(g)#adiocoina a lista gen[]

if len(alt) > 0:  
    maior = max(alt)
    menor = min(alt)
else:
    maior = 0
    menor = 0

homens = gen.count('m')
mulheres = gen.count('f')

print(f"\nMaior altura: {maior:.2f}")
print(f"Menor altura: {menor:.2f}")
print(f"Quantidade de homens: {homens}")
print(f"Quantidade de mulheres: {mulheres}")