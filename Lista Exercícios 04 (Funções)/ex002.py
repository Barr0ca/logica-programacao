def menorValor(numero01, numero02):
    if numero01 < numero02:
        return numero01
    else:
        return numero02
    
lista = []
for c in range(2):
    numero = float(input(f'Informe o {c+1}° número: '))
    lista.append(numero)
print(f'O menor entre os dois é {menorValor(lista[0], lista[1])}')