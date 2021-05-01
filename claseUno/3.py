# Hallar la longitud de la hipotenusa de un triangulo, teniendo como dato la medida de sus catetos 

from math import sqrt

cateto_adyacente = int(input("Ingrese el valor del cateto adyacente: "))

cateto_opuesto = int(input("Ingrese el valor del cateto opuesto: "))

hipotenusa = sqrt(((cateto_adyacente ** 2) + (cateto_opuesto ** 2)))


print ("La longitud de la hipotenusa es: %d " % (hipotenusa))