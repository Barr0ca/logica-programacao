def primo(numero):
    if numero == 1:
        return 0
    elif numero%2 == 0 and numero != 2:
        return 0
    elif numero%3 == 0 and numero != 3:
        return 0
    elif numero%5 == 0 and numero != 5:
        return 0
    elif numero%7 == 0 and numero != 7:
        return 0
    else:
        return 1
    
def main():
    numero = int(input('Informe um número: '))
    print('Caso o número seja primo saída: 1')
    print('Caso o número não seja primo saída: 0')
    print('')
    print(f'SAÍDA: {primo(numero)}')

main()