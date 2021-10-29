
"""
Se tiene una función llamada rand() que genera un número entre 0 y 1 de forma aleatoria y distribución uniforme. Implemente la función y calcule el número $\pi$.

Solucion:
La función que genera los números aleatorios se puede llamar dos veces, con lo cual se puede tener un par ordenado (x,y) 
Al llamarla en varias ocasiones se puede construir un cuadrado de lado 1 en el cuadrante 1 del plano

El objetivo consiste en contar todos los puntos dentro del circulo y dentro del cuadrado, con lo cual se puede obtener la siguiente aproximación:
pointsInCircle/pointsInSquare = areaCircle/areaSquare

Entre más puntos reciba la función para generar los número será mejor la aproximación.
Luego, para saber si un punto se encuentra dentro del círculo o no se mide la distancia del origen al punto, 
si la distancia es menor a 1 (radio del círculo) entonces el punto se encuentra en el círculo.

Despejando de la formula del area:
pointsInCircle/pointsInSquare = pi*r*r/4*r*r
pi = 4* (pointsCircle/pointsSquare)

"""

import random
import math
print('Ingrese el número de valores aleatorios que desea generar, n=', )
n = int(input())

def estimate_pi(n):
    num_point_circle = 0
    num_point_square = 0
    for _ in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        distance=math.sqrt(x**2+y**2)
        if distance <= 1:
            num_point_circle += 1
        num_point_square += 1
    return print('Valor de Pi:',4*num_point_circle/num_point_square)

estimate_pi(n)