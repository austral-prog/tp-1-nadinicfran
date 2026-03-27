from math import pi
import math

def circle():
    """
    Ejercicio 6 - Geometría de Círculo

    Dado el radio de un círculo, calcular e imprimir:
    1. El área (π × radio²)
    2. La circunferencia (2 × π × radio)
    """
    radio = 5
    pi =  math.pi

    area= (pi * radio * radio)
    print(area)
    circunferencia=(2 * pi * radio)
    print(circunferencia)

