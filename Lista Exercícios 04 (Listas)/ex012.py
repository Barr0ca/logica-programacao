lista = []
lista_pares = []
lista_impares = []
somatorio = 0

for c in range(5):
    numero = int(input(f'Informe o {c+1}° elemento: '))
    lista.append(numero)

for c in lista:
    somatorio += c

media = somatorio/5

for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
    else:
        lista_impares.append(c)

for c in lista_pares:
    maior_par = lista_pares[0]
    for c in lista_pares:
        if c > maior_par:
            maior_par = c

for c in lista_impares:
    menor_impar = lista_impares[0]
    for c in lista_impares:
        if c < menor_impar:
            menor_impar = c

if lista_pares == [ ]:
    print('Não tem número par.')
else:
    print(f'O maior número par é {maior_par}.')

if lista_impares == [ ]:
    print('Não tem número ímpar.')
else:
    print(f'O menor número ímpar é {menor_impar}.')
        
print(f'O somatório dos elementos é {somatorio} e a média é {media}.')
