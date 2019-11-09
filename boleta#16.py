# calculo del trabajo
# INPUT
fuerza=float(input("ingrese la fuerza en newton:"))
distancia=float(input("ingrese la distancia en m/s2:"))
tiempo=float(input("ingrese el tiempo en segundos:"))

# PROCESSING
trabajo= (fuerza*distancia)/tiempo
# OUTPUT
print("###################################")
print("  calculo para hallar el trabajo   ")
print("###################################")
print("fuerza=", fuerza)
print("distancia=", distancia)
print("tiempo=", tiempo)
print("###################################")
print("trabajo=", trabajo)
