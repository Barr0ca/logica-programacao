pares = []
impares = []
soma_numeros = 0
for c in range(5):
    numero = int(input(f'Informe o {c+1}° número: '))
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    soma_numeros += numero
media = soma_numeros/5
print(f'O maior número par é {max(pares)}; O menor número ímpar é {min(impares)}; O somatório dos números é {soma_numeros}; A média é {media}')