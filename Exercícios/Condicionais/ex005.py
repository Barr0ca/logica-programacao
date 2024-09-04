nome = input('Nome do produto: ')
valor = float(input('Valor do produto: '))
desconto = float(input('Desconto do produto (em %): '))

valor_desconto = valor*(desconto/100)
valor_com_desconto = valor - valor_desconto

print(f'\nPRODUTO: {nome}')
print(f'VALOR: {valor:.2f}')
print(f'DESCONTO: {desconto:.2f}%')
print(f'VALOR COM DESCONTO: {valor_com_desconto:.2f}')
