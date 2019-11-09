# DATOS Y CALCULO DEL TRIANGULO RECTANGULO
# INPUT
triangulo=input("ingrese el nombre del triangulo:")
cateto1=float(input("ingrese el cateto 1:"))
cateto2=float(input("ingrese el cateto 2:"))

# PROCESSING
import math
hipotenusa= math.sqrt(cateto1**2+cateto2**2)

# OUTPUT
print("######################################")
print("TRIANGULO:", triangulo)
print("######################################")
print("CATETO 1=", cateto1)
print("CATETO 2=", cateto2)
print("######################################")
print("HIPOTENUSA=", hipotenusa)
