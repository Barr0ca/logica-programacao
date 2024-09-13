print('--PRIMEIRA UNIDADE--')
notaU01 = float(input('Informe a nota (0.0 a 10): '))
frequenciaU01 = int(input('Informe a frequência (0 a 100): '))

print('\n--SEGUNDA UNIDADE--')
notaU02 = float(input('Informe a nota (0.0 a 10): '))
frequenciaU02 = int(input('Informe a frequência (0 a 100): '))
print(' ')

mediaNota = (notaU01+notaU02)/2
mediaFrequencia = (frequenciaU01+frequenciaU02)/2

if mediaFrequencia <= 75:
    print('Reprovado.')
elif mediaNota <= 3:
    print('Reprovado.')
elif notaU01 or notaU02 < 3:
    print('Reprovado.')
elif 3 <= mediaNota <= 7:
    print('Quarta Prova.')
else:
    print('Aprovado.')
          