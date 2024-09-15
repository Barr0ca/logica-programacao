def fatorialNumero(numero):
    fatorial = 1
    i = 0
    a = 1
    if numero < 0:
        return
    else:
        for c in range (numero, 1, -2):
            fatorial *= (numero-i)*(numero-a)
            i += 2
            a += 2
        return fatorial

numero = int(input('Informe o número para descobrir seu fatorial: '))
print(f'O fatorial desse número é {fatorialNumero(numero)}')
