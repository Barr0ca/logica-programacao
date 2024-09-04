valorX = float(input('Informe o valor de X: '))
if valorX <= 1:
    print('f(x): 1')
elif 1 < valorX <= 2:
    print('f(x): 2')
elif 2 < valorX <= 3:
    print(f'f(x): {valorX**2}')
else:
    print(f'f(x): {valorX**3}')