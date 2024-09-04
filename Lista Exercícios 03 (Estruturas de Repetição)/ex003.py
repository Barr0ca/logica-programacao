horas = -1
while True:
    print('FINALIZAR [0]')
    horas = int(
        input('Informe o total de horas trabalhadas: '))
    if horas != 0:
        valor_hora = float(input('Informe o valor-hora do trabalhador: '))
        if horas > 40:
            salario = (40*valor_hora) + ((40-valor_hora)*0.5)
            print(f'Salário: {salario}')
        else:
            salario = horas*valor_hora
            print(f'Salário: {salario}')
    if horas == 0:
        break