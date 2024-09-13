matriz01 = []
matriz01_linha01 = []
matriz01_linha02 = []

matriz02 = []
matriz02_linha01 = []
matriz02_linha02 = []

matriz03 = []
matriz03_linha01 = []
matriz03_linha02 = []

for c in range(2):
    numero = int(input(f'Informe o {c+1}° número da linha 1 da matriz 1: '))
    matriz01_linha01.append(numero)
matriz01.append(matriz01_linha01)
for c in range(2):
    numero = int(input(f'Informe o {c+1}° número da linha 2 da matriz 1: '))
    matriz01_linha02.append(numero)
matriz01.append(matriz01_linha02)

for c in range(2):
    numero = int(input(f'Informe o {c+1}° número da linha 1 da matriz 2: '))
    matriz02_linha01.append(numero)
matriz02.append(matriz02_linha01)
for c in range(2):
    numero = int(input(f'Informe o {c+1}° número da linha 2 da matriz 2: '))
    matriz02_linha02.append(numero)
matriz02.append(matriz02_linha02)

for c in range(2):
    numero01 = matriz01_linha01[c] + matriz02_linha01[c]
    numero02 = matriz01_linha02[c] + matriz02_linha02[c]
    matriz03_linha01.append(numero01)
    matriz03_linha02.append(numero02)

print('Matriz 1:')
print(matriz01_linha01)
print(matriz01_linha02)
print('')

print('Matriz 2:')
print(matriz02_linha01)
print(matriz02_linha02)
print('')

print('Matriz 3:')
print(matriz03_linha01)
print(matriz03_linha02)
