num = int(input("Digite um número inteiro: "))
if num <= 0:
    print(num)
elif (num % 3) and (num % 5) == 0:
    print("FizzBuzz")