# Ingresar un numero. Si es positivo calcular su raiz cuadrada, si es negativo mostrar su cuadrado y si es cero mostra "Error" ah ingresado un valor nulo.

from math import sqrt

numero = int(input("Ingrese un numero: "))

if numero > 0:
    raiz_cuadrada = sqrt (numero)
    print("La raiz cuadrada del numero ingresado es: %d " % (raiz_cuadrada))

if numero < 0:
    cuadrado = numero ** 2
    print("El cuadrado del numero ingresado es: %d" % (cuadrado))

if numero == 0:
    print  ("Error ah ingresado un valor nulo")
