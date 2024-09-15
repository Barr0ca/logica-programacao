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
    global opcao
    global lista
    while opcao != 0:
        opcao = exibeOpcoes()
        if opcao <= 0:
            print('Finalizando o programa...')
            break
        elif opcao == 1:
            for c in range(2):
                numero = float(input(f'Informe o {c+1}° número: '))
                lista.append(numero)
            print(f'O maior entre os dois é {maiorValorEntreDois(lista[0], lista[1])}')
        elif opcao == 2:
            for c in range(2):
                numero = float(input(f'Informe o {c+1}° número: '))
                lista.append(numero)
            print(f'O menor entre os dois é {menorValorEntreDois(lista[0], lista[1])}')
        elif opcao == 3:
            for c in range(3):
                numero = float(input(f'Informe o {c+1}° número: '))
                lista.append(numero)
            print(f'O maior entre os três é {maiorValorEntreTres(lista[0], lista[1], lista[2])}')
        elif opcao == 4:
            for c in range(3):
                numero = float(input(f'Informe o {c+1}° número: '))
                lista.append(numero)
            print(f'O menor entre os três é {menorValorEntreTres(lista[0], lista[1], lista[2])}')
        lista = [ ]

opcao = 1
lista = []

main()