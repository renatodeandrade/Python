num = int(input("Digite um número inteiro: "))
if num <= 0:
    print(num)
if (num % 3 and num % 5) == 0:
    print("FizzBuzz")
else:
    print(num)