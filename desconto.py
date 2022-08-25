preço_total = float(input('Digite o preço do produto: '))
desconto = preço_total*5/100
print(f'O produto custava R$ {preço_total:.2f} e recebeu um desconto de 5%, agora custando R$ {preço_total-desconto:.2f}.')