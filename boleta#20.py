# CALCULO DEL AREA DEL TRAPECIO
# INPUT
print("trapecio")
base_menor=float(input("ingrese la base menor:"))
base_mayor=float(input("ingrese la base mayor:"))
haltura=float(input("ingrese la haltura:"))

# PROCESSING
area= (base_menor+base_mayor)*haltura/2

# OUTPUT
print("####################################")
print("        AREA DEL TRAPECIO           ")
print("####################################")
print("BASE MENOR=", base_menor,      "BASE MAYOR=", base_mayor)
print("HALTURA=", haltura)
print("####################################")
print("AREA=", area)