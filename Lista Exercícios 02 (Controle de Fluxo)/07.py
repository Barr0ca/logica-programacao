ladoA = float(input('Informe o A lado do triângulo: '))
ladoB = float(input('Informe o B lado do triângulo: '))
ladoC = float(input('Informe o C lado do triângulo: '))

if ladoA > abs(ladoB-ladoC) and ladoA < ladoB+ladoC:
    print('Sim, com esses lados pode-se formar um triângulo.')
else:
    print('Não dá para formar um triângulo com estes lados.')