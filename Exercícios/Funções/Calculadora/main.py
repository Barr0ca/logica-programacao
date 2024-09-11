def menu():
    print('### MENU ###')
    print('0 - SAIR')
    print('1 - SOMAR')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def somar(numero01, numero02):
    resultado = numero01+numero02
    return resultado

def subtrair(numero01, numero02):
    resultado = numero01-numero02
    return resultado

def multiplicar(numero01, numero02):
    resultado = numero01*numero02
    return resultado

def dividir(numero01, numero02):
    resultado = numero01/numero02
    return resultado

opcao = 1
numero01 = 0
numero02 = 0
resultado = 0

while opcao != 0:
    opcao = menu()
    if opcao <= 0:
        print('Finalizando o programa...')
        break
    numero01 = float(input('Informe o 1° número: '))
    numero02 = float(input('Informe o 2° número: '))
    if opcao == 1:
        resultado = somar(numero01, numero02)
    print(f'Resultado: {resultado}')