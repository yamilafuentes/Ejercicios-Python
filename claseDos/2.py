#  Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.

positive = 0

flak = True

while flak:
    num = int(input("Ingrese un numero: ")) 
    if num == 0:
        flak = False
    if num > 0:
        positive += 1
    


print(positive)





