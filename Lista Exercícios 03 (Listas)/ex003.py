lista = []
qtd_numeros = int(input('Informe a quantidade de números a serem lidos: '))
impares = 0
for c in range(qtd_numeros):
    numero = int(input(f'Informe o {c+1}° número: '))
    if numero%2 != 0:
        impares += 1
    lista.append(numero)
print(f'Existem {impares} números ímpares na lista.')