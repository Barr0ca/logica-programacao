def menu():
    print('')
    print('0 - SAIR')
    print('1 - A VISTA (10% DESCONTO)')
    print('2 - DUAS VEZES (VALOR DE ETIQUETA)')
    print('3 - TRÊS A DEZ VEZES (3% DE JUROS POR MÊS, COMPRAS ACIMA DE R$ 100,00)')
    print('4 - TOTAL GASTO')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def aVista(valor_produto):
    return float(valor_produto-(valor_produto*0.1))

def duasVezes(valor_produto):
    return float(valor_produto/2)

def comJuros(valor_produto, prestacoes):
    if prestacoes == 1:
        return (valor_produto-(valor_produto*0.1))/prestacoes
    elif prestacoes == 2:
        return valor_produto/prestacoes
    else:
        if valor_produto < 100:
            return valor_produto/prestacoes
        else:
            return (valor_produto*1.03)/prestacoes 

opcao = 1
total_gasto = 0
valor_produto = 0

while opcao != 0:
    opcao = menu()

    if opcao == 1:
        valor_produto = float(input('Informe o valor do produto a ser comprado: R$ '))
        print(f'O valor do produto ficou R$ {aVista(valor_produto):.2f} a vista.')
        valor_produto = valor_produto-(valor_produto*0.1)

    elif opcao == 2:
        valor_produto = float(input('Informe o valor do produto a ser comprado: R$ '))
        print(f'O valor do produto ficou R$ {valor_produto:.2f} dividido em 2 de R$ {duasVezes(valor_produto):.2f}')

    elif opcao == 3:
        valor_produto = float(input('Informe o valor do produto a ser comprado: R$ '))
        prestacoes = int(input('Informe a quantidade de vezes que quer dividir (3 a 10 vezes): '))
        print(f'O valor do produto ficou {(comJuros(valor_produto, prestacoes)*prestacoes):.2f}, dividido em {prestacoes} de R$ {comJuros(valor_produto, prestacoes):.2f} ')
        if valor_produto > 100:
            valor_produto = valor_produto*1.03
        if prestacoes == 1:
            valor_produto = valor_produto-(valor_produto*0.1)

    elif opcao == 4:
        print(f'Você gastou R$ {total_gasto:.2f} até agora na loja.')

    total_gasto += valor_produto
    valor_produto = 0
