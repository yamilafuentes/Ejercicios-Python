# Ingresar dos números, calcular y mostrar el cociente del primero por el segundo, siempre que el divisor no sea cero. En este 
# último caso mostrar la leyenda “no se puede realizar el cociente”. 


numero1 = float(input("Ingresar el primer numero: "))
numero2 = float(input("Ingresar el segundo numero: "))

if numero2 != 0:
    cociente = numero1 / numero2
else:  
    print("No se puede realizar el cociente ")

