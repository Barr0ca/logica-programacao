lista = []
lista_invertida = []
auxiliar = 0
for c in range(20):
    elemento = input(f'Informe o {c+1}° elemento: ')
    lista.append(elemento)
print('Sua lista:')
for c in lista:
    print(c)
for c in range(19, -1, -1):
    auxiliar = lista[c]
    lista_invertida.append(auxiliar)
print('Sua nova lista:')
for i in lista_invertida:
    print(i)
