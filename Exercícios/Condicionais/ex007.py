n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
print('--OPERAÇÕES--\n--SOMA-1\n--SUBTRAÇÃO-2\n--MULTIPLICAÇÃO-3\n--DIVISÃO-4\nObservação: Ordem de precedência das operações sera 1° depois o 2° número')
opcao = int(input('OPÇÃO:'))
if opcao == 1:
    soma = n1+n2
    print(f'A soma entre os números é {soma}')
elif opcao == 2:
    subtracao = n1-n2
    print(f'A subtração entre os números é {subtracao}')
elif opcao == 3:
    multiplicacao = n1*n2
    print(f'A multiplicação entre os números é {multiplicacao}')
elif opcao == 4:
    if n2 == 0:
        print('Não dividirás por 0!!')
    else:
        divisao = n1/n2
        print(f'A divisão entre os números é {divisao}')
else:
    print('Opção inválida.')
