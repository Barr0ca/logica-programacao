ladoA = float(input('Informe o A lado do triângulo: '))
ladoB = float(input('Informe o B lado do triângulo: '))
ladoC = float(input('Informe o C lado do triângulo: '))

if ladoA > abs(ladoB-ladoC) and ladoA < ladoB+ladoC:
    print('Sim, com esses lados pode-se formar um triângulo.')
    if (ladoA+ladoB)/ladoC == 2:
        print('TIPO: EQUILÁTERO')
    elif (ladoA == ladoB or ladoA == ladoC) and (ladoA != ladoB or ladoC):
        print('TIPO: ISÓSCELES')
    else:
        print('TIPO: ESCALENO')
else:
    print('Não dá para formar um triângulo com estes lados.')