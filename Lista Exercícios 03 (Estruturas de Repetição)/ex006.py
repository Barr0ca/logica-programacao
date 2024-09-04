num = 0
maior = 0
segundo_maior = 0
for c in range(10):
    num = float(input(f'Informe o {c+1}° número: '))
    if num > maior:
        segundo_maior = maior
        maior = num
    elif num > segundo_maior:
        segundo_maior = num
print(f'Maior: {maior} Segundo maior: {segundo_maior}')
