qtd_total_acais = 0
lucro_total = 0

for dia in range(3, 0, -1):
    qtd_acai = int(input(f'Informe a quantidade de açaís vendidos há {dia} dia(s) atrás: '))
    qtd_total_acais += qtd_acai
    lucro_total += qtd_acai*3
    print(f'Foram vendidos há {dia} dia(s) {qtd_acai} açaís. Lucro: R$ {(qtd_acai*3):.2f}\n') 
    
print(f'Ao fim dos 3 dias o lucro total foi de R$ {lucro_total:.2f} e um total de {qtd_total_acais} açaís vendidos.')