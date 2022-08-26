quilômetros = float(input('Quantos quilômetros foram rodados? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
print(f'Foram rodados {quilômetros} quilômetros durante o período de {dias} dias. Sendo assim, o valor total a ser pago é de R$ {(quilômetros*0.15) + (dias*60):.2f}.')