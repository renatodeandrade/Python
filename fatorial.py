numero = int(input("Digite um número inteiro: "))
resultado = 1
count = 1
while count <= numero:
    resultado *= count
    count += 1
print(resultado)