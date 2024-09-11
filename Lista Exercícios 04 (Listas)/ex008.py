lista = []
pares = 0
for c in range(20):
    numero = int(input(f'Informe o {c+1}° número: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares += 1
for c in lista:
    print(c)
print(f'Existem {pares} números pares na lista.')