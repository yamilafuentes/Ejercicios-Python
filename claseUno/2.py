# Calcular el importe que debe pagar una persona si compra una heladera de pesos X y por pagar en efectivo le hacen el %10 de descuento. ¿Cuanto abona?

precio_heladera = int(input("¿Cuanto pago por su heladera? "))

descuento = (precio_heladera * 10) / 100 

nuevo_precio = precio_heladera -  descuento

print ("Usted debe pagar %d" % (nuevo_precio))

