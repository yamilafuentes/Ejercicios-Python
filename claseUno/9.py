# Se ingresa el código de tipo de llamada: 
# 1: Local 
# 2: Interurbana 
# 3: Internacional 
# y la duración en minutos de la misma. Si el minuto cuesta $0.25 para la llamada local, $0.40 para la llamada interurbana y 
# $1.05 para la llamada internacional, diseñar un algoritmo que permita calcular el monto a pagar por dicha llamada. 


min_call = int(input("¿Cuantos minutos hablaste por telefono? "))

tipe_call = input("Si es local presione 1, si es interurbana presione 2 y si es internacional presiones 3: ")

dicc = {"1": 0.25, "2": 0.40, "3": 1.05}

value_call = min_call * dicc[tipe_call]

print("El valor de su llamada es ${}" .format(value_call))


