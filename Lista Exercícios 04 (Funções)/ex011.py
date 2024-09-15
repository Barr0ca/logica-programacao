def primo(numero):
    soma_primos = 0
    for c in range(numero+1):
        if c == 1:
            c = 0
        elif c%2 == 0 and c != 2:
            c = 0
        elif c%3 == 0 and c != 3:
            c = 0
        elif c%5 == 0 and c != 5:
            c = 0
        elif c%7 == 0 and c != 7:
            c = 0
        soma_primos += c
    return soma_primos

def main():
    numero = int(input('Informe um número: '))
    print('')
    print(f'A soma dos numeros primos até {numero} é igual a {primo(numero)}')

main()
