# NUMERO DE APROBADOS EN LA carrera
# INPUT
carrera=input("ingrese la carrera universitaria:")
cantidad_alumnos=int(input("ingrese la cantidad de estudiantes:"))
nota_aprob=float(input("ingrese la nota aprobatoria:"))

# PROCESSING
aprobados= (cantidad_alumnos/nota_aprob)

# OUTPUT
print("#####################################")
print("      aprobados en la carrera"        )
print("#####################################")
print(" carrera universitaria:", carrera)
print("######################################")
print("cantidad de alumnos=", cantidad_alumnos)
print("notas aprobatorias=", nota_aprob)
print("######################################")
print("numero de aprobados=", aprobados)