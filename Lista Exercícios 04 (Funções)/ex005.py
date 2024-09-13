def exibeOpcoes():
    print('')
    print('0 - SAIR')
    print('1 - MAIOR ENTRE DOIS NÚMEROS')
    print('2 - MENOR ENTRE DOIS NÚMEROS')
    print('3 - MAIOR ENTRE TRÊS NÚMEROS')
    print('4 - MENOR ENTRE TRÊS NÚMEROS')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def maiorValorEntreDois(numero01, numero02):
    if numero01 > numero02:
        return numero01
    else:
        return numero02

def menorValorEntreDois(numero01, numero02):
    if numero01 < numero02:
        return numero01
    else:
        return numero02
    
def maiorValorEntreTres(numero01, numero02, numero03):
    if numero01 > numero02 and numero01 > numero03:
        return numero01
    elif numero02 > numero01 and numero02 > numero03:
        return numero02
    else:
        return numero03
    
def menorValorEntreTres(numero01, numero02, numero03):
    if numero01 < numero02 and numero01 < numero03:
        return numero01
    elif numero02 < numero01 and numero02 < numero03:
        return numero02
    else:
        return numero03

def main():
    exibeOpcoes()
    if exibeOpcoes() == 1:
        maiorValorEntreDois()
    elif exibeOpcoes() == 2:
        menorValorEntreDois()
    elif exibeOpcoes() == 3:
        maiorValorEntreTres()
    elif exibeOpcoes() == 4:
        menorValorEntreTres()
    elif exibeOpcoes() == 0:
        return

opcao = 1

while opcao != 0:
    opcao = exibeOpcoes()
    main()