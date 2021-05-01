# Calcular el promedio semanal de gastos en un mes, ingresando como datos:
#    Semana número
#    Gasto semanal 
# El proceso termina cuando “semana número” es igual a 5.


week = 1
total_cost = 0

while week < 5:
    cost = float(input("¿Cuanto gastaste esta semana {}? " .format(week)))
    total_cost += cost  
    week += 1

print("El promedio de gasto semanal es: {} " .format(total_cost / (week - 1)))


