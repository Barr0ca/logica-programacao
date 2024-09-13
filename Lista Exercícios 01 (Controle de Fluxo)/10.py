frequencia = int(input('Informe a frequencia do aluno, em % (0 a 100): '))
if frequencia <= 75:
    print('Reprovado.')
else:
    nota = float(input('Informe a nota do aluno (0.0 a 10): '))
    if nota <= 3:
        print('Reprovado.')
    elif nota > 3 and nota <=7:
        print('Quarta prova.')
    else:
        print('Aprovado.')
