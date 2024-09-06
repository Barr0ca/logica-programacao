a = []
qtd_numeros = int(input('Informe a quantidade de números a serem lidos: '))
ocorrencia = 0
for c in range(qtd_numeros):
    numero = int(input(f'Informe o {c+1}° número: '))
    a.append(numero)
numero_ocorrencia = int(input('Informe um numero para verificar sua ocorrência na lista: '))
for c in a:
    if c == numero_ocorrencia:
        ocorrencia += 1
print(f'Esse número aparece {ocorrencia} vezes na lista.')