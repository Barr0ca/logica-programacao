abaixo = []
na_media = [] 
qtd_alunos = int(input('Informe o número de alunos: '))
for c in range(qtd_alunos):
    nota_aluno = int(input(f'Informe a nota do {c+1}° aluno: '))
    if nota_aluno < 60:
        abaixo.append(nota_aluno)
    else:
        na_media.append(nota_aluno)
print(f'A quantidade de alunos que estão abaixo da média é de {len(abaixo)} alunos \nA quantidade de alunos que estão na média é de {len(abaixo)} alunos')