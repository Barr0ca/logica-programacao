def maiorValor(numero01, numero02, numero03):
    if numero01 > numero02 and numero01 > numero03:
        return numero01
    elif numero02 > numero01 and numero02 > numero03:
        return numero02
    else:
        return numero03
    
lista = []
for c in range(3):
    numero = float(input(f'Informe o {c+1}° número: '))
    lista.append(numero)
print(f'O maior entre os três é {maiorValor(lista[0], lista[1], lista[2])}')