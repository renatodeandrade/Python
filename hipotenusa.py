#ateto_oposto = float(input('Insira o valor do cateto oposto: '))
#cateto_adjacente = float(input('Insira o valor do cateto adjacente: '))
#hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
#print(f'A hipotenusa equivale a {hipotenusa:.2f}.')
import math
cateto_oposto = float(input('Insira o valor do cateto oposto: '))
cateto_adjacente = float(input('Insira o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa equivale a {hipotenusa:.2f}.')