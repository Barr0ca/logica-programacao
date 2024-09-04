lados_quadrado = int(input('Informe os lados do quadrado (1 a 20): '))
print('*'*lados_quadrado)
for c in range(lados_quadrado-2):
    print('*' + (' '*(lados_quadrado-2)) + '*')
print('*'*lados_quadrado)