lista = []
i = 0
for c in range(15):
    numero = input(f'Informe o {c+1}° elemento: ')
    lista.append(numero)
for c in lista:
    print(f'O elemento da posição {i+1} é {c}.')
    i += 1
