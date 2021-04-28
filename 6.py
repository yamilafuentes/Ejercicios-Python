# Ingrese las edades de 2 personas. Si una de ellas es mayor de edad y la otra menor de edad, calcular y mostrar el promedio, en caso contrario mostrar las edades.

edad1 = int(input("Ingrese la edad de la primer persona: "))

edad2 = int(input("Ingrese la edad de la segunda persona: "))

if (edad1 > edad2) or (edad1 < edad2):
    promedio_edades = (edad1 + edad2) / 2
    print("El promedio de las edades ingresadas es: %d " % (promedio_edades))
else:
    print ("Las edades son %d y %d años " % (edad1, edad2))


