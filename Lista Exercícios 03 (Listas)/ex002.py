lista = []
for c in range(10):
    numero = int(input(f'Informe o {c+1}° número: '))
    if numero%2 == 0:
        numero = 1
    else:
        numero = -1
    lista.append(numero)
for c in lista:
    print(c)