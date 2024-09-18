def menu():
    print('')
    print('0 - SAIR')
    print('1 - ACENDER UMA LÂMPADA')
    print('2 - APAGAR UMA LÂMPADA')
    print('3 - CONSULTAR ESTADO ATUAL DE UMA LÂMPADA')
    print('4 - CONSULTAR ESTADO DE TODAS AS LÂMPADAS')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def acender_lampada(pos_lampada):
    global lista_lampadas
    lista_lampadas[pos_lampada] = True

def apagar_lampada(pos_lampada):
    global lista_lampadas
    lista_lampadas[pos_lampada] = False

def exibir_status(pos_lampada):
    if lista_lampadas[pos_lampada]:
        print(f'A lâmpada está acessa.')
    else:
        print(f'A lâmpada está apagada.')

def exibir_status_total():
    for c in range(20):
        if lista_lampadas[c]:
            print(f'A {c}° lâmpada está acessa.')
        else:
            print(f'A {c}° lâmpada está apagada.')

opcao = 1
lista_lampadas = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

while opcao != 0:
    opcao = menu()
    if opcao <= 0:
        print('Finalizando o programa...')
        break
    if opcao == 1:
        pos = int(input('Informe a lâmpada que será acessa (0 - 19): '))
        acender_lampada(pos)
        print(f'Lâmpada na posição {pos} acessa.')
    elif opcao == 2:
        pos = int(input('Informe a lâmpada que será apagada (0 - 19): '))
        apagar_lampada(pos)
        print(f'Lâmpada na posição {pos} apagada.')
    elif opcao == 3:
        pos = int(input('Informe a lâmpada para ver os status dela (0 - 19): '))
        exibir_status(pos)
    elif opcao == 4:
        exibir_status_total()