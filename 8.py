# Calcular el importe que debe pagar un auto en un estacionamiento teniendo en cuenta como datos las horas y minutos de uso. 
# El valor de la hora es de $45 y si los minutos exceden de 15 se incrementa una hora al importe. El mínimo a cobrar es de una hora.


min_value = 0.75

hours_car_parking= int(input("Ingrese solamente las horas que utilizo el estacionamiento: "))
min_car_parking= int(input("Ingrese solamente los minutos que utilizo el estacionamiento: "))

hour_in_min = 60

hours_car_parking += int(min_car_parking / hour_in_min)
min_car_parking = min_car_parking % hour_in_min


hour_to_min = hours_car_parking * hour_in_min 

if min_car_parking > 15:
    min_car_parking = hour_in_min 

import_value = (min_car_parking + hour_to_min) * min_value

print("El importe a cobrar es de ${}" .format(import_value))





