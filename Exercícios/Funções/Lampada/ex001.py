def menu():
    print('')
    print('0 - SAIR')
    print('1 - ACENDER A LUZ')
    print('2 - APAGAR A LUZ')
    print('3 - CONSULTAR ESTADO ATUAL')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def acender_lampada():
    global lampada
    lampada = True

def apagar_lampada():
    global lampada
    lampada = False

def exibir_status():
    if lampada:
        print(f'A lâmpada está acessa.')
    else:
        print(f'A lâmpada está apagada.')

opcao = 1
lampada = False

while opcao != 0:
    opcao = menu()
    if opcao <= 0:
        print('Finalizando o programa...')
        break
    if opcao == 1:
        acender_lampada()
        print('Lâmpada acessa.')
    elif opcao == 2:
        apagar_lampada()
        print('Lâmpada apagada.')
    elif opcao == 3:
        exibir_status()