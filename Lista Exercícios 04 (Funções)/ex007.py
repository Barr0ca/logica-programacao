def enesimaPotencia(numero, potencia):
    return numero**potencia

numero = float(input('Informe um número real: '))
potencia = float(input('Informe a potencia: '))
print(f'{numero} elevado a {potencia} é {enesimaPotencia(numero, potencia)}')