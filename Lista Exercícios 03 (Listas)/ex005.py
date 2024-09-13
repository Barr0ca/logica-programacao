impares = []
pares = []
for c in range(30):
    numero = int(input(f'Informe o {c+1}° número: '))
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    if len(impares) == 5:
        for c in impares:
            print(c)
        impares = []
    elif len(pares) == 5:
        for c in pares:
            print(c)
        pares = []