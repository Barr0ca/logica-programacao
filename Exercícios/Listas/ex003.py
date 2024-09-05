a = []
maior = 0
menor = 0
for c in range(10):
    numero = int(input(f'Digite o {c+1}° número: '))
    a.append(numero)
for c in range(len(a)):
    if c == 0:
        maior = a[c]
        menor = a[c]
    else:
        if a[c] > maior:
            maior = a[c]
        elif a[c] < menor:
            menor = a[c]
print(f'O maior número dessa lista é {maior} e o menor é {menor}')