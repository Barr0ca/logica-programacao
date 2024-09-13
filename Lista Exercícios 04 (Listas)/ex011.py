numero_alunos = int(input('Informe a quantidade de alunos a serem avaliados: '))
notas = []
for c in range(numero_alunos):
    nota = int(input(f'Informe a nota do {c+1}° aluno: '))
    notas.append(nota)
for c in notas:
    contador = 0
    for n in notas:
        if n == c:
            contador += 1
    print(f'A nota {c} aparece {contador} vezes.')