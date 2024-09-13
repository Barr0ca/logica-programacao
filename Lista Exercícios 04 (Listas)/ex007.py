k = []
for c in range(30):
    numero = input(f'Informe o {c+1}° elemento: ')
    k.append(numero)
print(k)

for c in range(29):
    k[c] = k[c+1]
print(k)