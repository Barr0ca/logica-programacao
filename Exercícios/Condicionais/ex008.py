salario = float(input('Informe o salário do cliente: '))
emprestimo = float(input('Informe o valor do empréstimo: '))
tempo = int(input('Informe os meses a serem pago o empréstimo: '))
prestacao = emprestimo/tempo
if prestacao > salario*0.3:
    print('Infelizmente o valor da prestação é maior que 30% do seu salário, empréstimo inválido')
else:
    print(f'Empréstimo aceito, suas parcelas ficaram no valor de R$ {prestacao:.2f} a serem pagas em {tempo} meses.')