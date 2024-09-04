print('Informe o tipo de instalação:\n(R) Residência\n(I) Indústria\n(C) Comércio')
zona = input('Opção: ')
kwh = int(input('Informe o gasto de energia elétrica (em KW/h): '))
if zona.lower() == 'r':
    if kwh <= 500:
        precoEnergia = kwh*0.4
        print(f'Valor a ser pago: R$ {float(precoEnergia):.2f}')
    else:
        precoEnergia = (500*0.4)+((kwh-500)*0.65)
        print(f'Valor a ser pago: R$ {float(precoEnergia):.2f}')
elif zona.lower() == 'i':
    if kwh <= 5000:
        precoEnergia = kwh*0.55
        print(f'Valor a ser pago: R$ {float(precoEnergia):.2f}')
    else:
        precoEnergia = (5000*0.55)+((kwh-5000)*0.60)
        print(f'Valor a ser pago: R$ {float(precoEnergia):.2f}')
elif zona.lower() == 'c':
    if kwh <= 1000:
        precoEnergia = kwh*0.55
        print(f'Valor a ser pago: R$ {float(precoEnergia):.2f}')
    else:
        precoEnergia = (1000*0.55)+((kwh-1000)*0.60)
        print(f'Valor a ser pago: R$ {float(precoEnergia):.2f}')