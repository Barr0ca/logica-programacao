vendas = -1
while True:
    print('FINALIZAR [0]')
    vendas = float(
        input('Informe o total da renda das vendas da última semana: R$ '))
    salario = 200 + (vendas * 0.09)
    if vendas == 0:
        break
    elif vendas != 0: 
        print(f'Salário: R$ {salario}')
