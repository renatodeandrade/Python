from cmath import cos, tan
from math import sin, cos, tan, radians
angulo = float(input('Insira um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} graus tem seno de {seno:.2f}, cosseno de {cosseno:.2f} e tangente de {tangente:.2f}.')