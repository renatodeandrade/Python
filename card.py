meuCartão = int(input("Digite o número do seu cartão de crédito: "))
cartãoLido = 1
CartãoEncontrado = False
while cartãoLido != 0 and not CartãoEncontrado:
    cartãoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartãoLido == meuCartão:
        CartãoEncontrado = True
if CartãoEncontrado:
    print("Cartão encontrado!")
else:
    print("Meu cartão não está lá.")