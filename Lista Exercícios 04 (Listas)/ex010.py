s = []
for c in range(20):
    elemento = input(f'Informe o {c+1}° elemento: ')
    s.append(elemento)
a = int(input('Informe o valor da variável "a": '))
for c in s:
    print(c*a)
