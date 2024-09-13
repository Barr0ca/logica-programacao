# Estruturas condicionais

# Exemplo 001
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# if n1 > n2:
#     print('O primeiro número é maior.')
# else:
#     print('O segundo número é o maior.')

# Exemplo 002
# n1 = int(input('Digite um número: '))
# if n1 > 0:
#     print('O número é positivo.')
# else:
#     print('O número é negativo.')

# Exemplo 003
# n1 = int(input('Digite um número: '))
# if n1 > 10 and n1 < 20:
#     print('O número digitado está entre 10 e 20.')
# else:
#     print('O número digitado NÃO está entre 10 e 20.')

# Exemplo 004
# n1 = int(input('Digite um número: '))
# if n1 == 0 or n1 == 1:
#     print('Você digitou um binário.')
# else:
#     print('Não é um binário.')

# Exemplo 005
# categoria = int(input('Informe a categoria do produto: '))
# preco = 0
# if categoria == 1:
#     preco = 10
# else:
#     if categoria == 2:
#         preco = 18
#     else:
#         if categoria == 3:
#             preco = 23
#         else:
#             if categoria == 4:
#                 preco = 26
#             else:
#                 if categoria == 5:
#                     preco = 31
#                 else:
#                     print('Opção inválida.')
# print(f'O valor do produto é R$ {preco}')

# Exemplo 006
# opcao = int(input('Escolha uma categoria, de 1 a 5, para saber seu preço: '))
# preco = 0
# if opcao == 1:
#     preco = 10
# elif opcao == 2:
#     preco = 18
# elif opcao == 3:
#     preco = 23
# elif opcao == 4:
#     preco = 26
# elif opcao == 5:
#     preco = 31
# else:
#     print('Não é uma opção válida!')
# print(f'O valor dessa categoria é R$ {preco}')

# Exemplo 007
# qtd_acais3 = int(input('Quantos açaís foram vendidos trás-anteontem? '))
# qtd_acais2 = int(input('Quantos açaís foram vendidos anteontem? '))
# qtd_acais1 = int(input('Quantos açaís foram vendidos ontem? '))
# valor1 = qtd_acais1*3
# valor2 = qtd_acais2*3
# valor3 = qtd_acais3*3
# valor_total = valor1+valor2+valor3
# print(f'\nO valor obtido  trás-anteontem foi de R$ {valor3:.2f}\nO valor obtido  anteontem foi de R$ {valor2:.2f}\nO valor obtido  ontem foi de R$ {valor1:.2f}\nO valor obtido nos últimos 3 dias foi de R$ {valor_total:.2f}')

# Exemplo 008
# alunos = []
# quantidade = int(input('Informe a quantidade de alunos a serem registrados: '))
# for c in range(quantidade):
#     alunos.append(input('Informe o nome do aluno: '))
# print(f'\nAlunos registrados na turma:')
# for c in range(quantidade):
#     print(f'Aluno {c+1}: {alunos[c]}')

# Exemplo 009
# lista = [10, 20, 30, 40, 50]
# elemento_removido = lista.pop(2)
# print(f'Elemento removido: {elemento_removido}')
# for c in range(4):
#     print(lista[c])

# Exemplo 010
# lista = []
# lista.append('João')
# lista.append('Chico')
# lista.append('Antônio')
# lista.append('Jeff')
# i=0
# while i<4:
#     print(lista[i])
#     i+=1

# Exemplo 011
# lista = ['algoritimo','é','muito','bom']
# lista.insert(2, 'realmente')
# i=0
# while i<5:
#     print(lista[i])
#     i+=1

# Exemplo 012
# lista = [10, 20, 30, 40, 50]
# del lista[2]
# i=0
# while i<4:
#     print(lista[i])
#     i+=1

# Exemplo 013
# lista = [10, 50, 5, 2, 100]
# elemento_removido = lista.pop(2)
# print(f'Elemento removido: {elemento_removido}')
# i=0
# while i<4:
#     print(lista[i])
#     i+=1

# Exemplo 014
# lista = [10, 50, 5, 2, 100]
# lista.remove(5)
# i=0
# while i<4:
#     print(lista[i])
#     i+=1

# Exemplo 015
# lista = ['algoritimo','é','muito','bom']
# lista.remove('muito')
# i=0
# while i<3:
#     print(lista[i])
#     i+=1

# Exemplo 016
# lista = [10, 50, 5, 2, 100]
# tamanho = len(lista)
# print(f'O tamanho da lista é: {tamanho}')

# Exemplo 017
# lista = [10, 50, 5, 2, 100]
# i = 0
# for c in lista:
#     print(f'Elemento {i}: {c}')
#     i+=1

# Exemplo 018
# def quadrado(numero):
#     return numero*numero
# print(quadrado(5))

# Exemplo 019
# def quadrado(numero):
#     return numero**2
# def imprime_quadrado(numero):
#     if numero<=1:
#         return
#     print(quadrado(numero))
# num_quadrado = 0
# for c in range(6):
#     imprime_quadrado(c)

# Exemplo 020
# def func():
#     global x
#     x=1
#     return print(x)

# x = 42
# print(x)
# func()
# print(x)