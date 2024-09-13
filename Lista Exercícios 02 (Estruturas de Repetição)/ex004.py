num = 0
maior = 0
for c in range(10):
    num = float(input(f'Informe o {c+1}° número: '))
    if num > maior:
        maior = num
print(f'O maior número: {maior}')