# PROMEDIO DE NOTAS DEL ALUMNO
# INPUT
alumno=input("ingrese el nombre del alumno:")
not1=float(input("ingrese la nota 1:"))
not2=float(input("ingrese la nota 2:"))
not3=float(input("ingrese la nota 3:"))
not4=float(input("ingrese la nota 4:"))

# PROCESSING
promedio= (not1+not2+not3+not4)/4

# OUTPUT
print("#####################################")
print("         promedio de notas           ")
print("#####################################")
print("NOTA 1=", not1,        "NOTA 2=", not2)
print("NOTA 3=", not3,        "NOTA 4=", not4)
print("#####################################")
print("PROMEDIO=", promedio)