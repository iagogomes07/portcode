print('Bem vindo, marque seu corte ou cadastre sua empresa')
interface = int(input('[1] sou cliente e [2] para cadastrar a empresa:'))

if interface == 2:
    while True:
        nmbrb = str(input('Digite o nome da sua empresa:'))
        end = str(input('Digite o endereço da sua empresa:'))
        cnpj = str(input('Digite o CNPJ da sua empresa:'))
        print('Confirme as informações\n', nmbrb, '\n', end, '\n', cnpj)
        a = int(input('[1] para sim e [2] para não:'))
        if a == 1:
            print('Insira o horario de funcionamento (24 hrs)')
            d = int(input('insira o horario de abertura: '))
            b = int(input('insira o horario de fechamento: '))
            c = int(input('insira o intervalo entre horarios: '))
            for a in range(d, b + 1, c):
                if d < b - 1:
                    print('')
                    print(a,": 00,")
                else:
                    print(a,": 00.")
            print('Tmj parceirão')
            break

elif interface == 1:
    nome = str(input('Digite seu nome'))
    end = str(input('Digite seu endereço'))
    cpf = str(input('Digite seu CPF'))

else:
    print('man')
