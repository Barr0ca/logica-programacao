lista_a = []
lista_b = []
lista_resultado = []
for c in range(10):
    numeros_a = int(input(f'Informe o {c+1}° elemento da 1° lista: '))
    lista_a.append(numeros_a)
for c in range(10):
    numeros_b = int(input(f'Informe o {c+1}° elemento da 2° lista: '))
    lista_b.append(numeros_b)
for c in range(10):
    numeros_resultado = lista_a[c]*lista_b[c]
    lista_resultado.append(numeros_resultado)
for c in lista_resultado:
    print(c)