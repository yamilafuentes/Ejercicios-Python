# Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo de cada curso:
#    Curso (1-5)
#    Presentes
#    Ausentes
#Calcular
#    Por cada curso el porcentaje de presentes sobre el total
#    Cantidad de ausentes en el colegio
#    Curso con mayor cantidad de ausente


course_highest_absentees = 0
absentees_college = 0
course = 0

for curso in range(5):
    course += 1
    number_students = int(input("Ingrese el numero de estudianes del curso numero {}: " .format(course)))
    present = int(input("Alumnos presentes en el curso: "))
    absent = int(input("Alumnos ausentes en el curso: "))
    absentees_college += absent

    present_percentage = int((present * 100 ) / number_students)

    print("En el curso numero {} el porcentaje de presentes es del: {}%" .format(course, present_percentage))

print("La cantidad de ausentes en el colegio es {}" .format(absentees_college))





