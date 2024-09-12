lista = []
lista_pares = []
for c in range(5):
    numero = input(f'Informe o {c+1}° elemento: ')
    lista.append(numero)
for c in lista:
    if c%2 == 0:
        lista_pares.append(c)
        
