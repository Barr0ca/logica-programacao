k = []
for c in range(30):
    numero = input(f'Informe o {c+1}° elemento: ')
    k.append(numero)
print(k)

for c in range((len(k))-1):
    if c % 2 != 0:
        aux = k[c]
        k[c] = k[c+1]
        k[c+1] = aux
print(k)