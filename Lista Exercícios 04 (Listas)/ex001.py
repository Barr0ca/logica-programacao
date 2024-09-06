lista = []
auxiliar = 0
for c in range(10):
    numero = int(input(f'Informe o {c+1}° número: '))
    lista.insert(auxiliar, numero)
    auxiliar -= 1
for c in lista:
    print(c)