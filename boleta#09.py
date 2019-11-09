# VOLUMEN DE LA ESFERA
# INPUT
print("   ESFERA GOMETRICA    ")
cuerpo_geometrico=input("ingrese la figura geometrica:")
radio=float(input("ingrese el radio de la esfera en cm:"))

# PROCESSING
pi= 3.14
volumen= 4*pi*(radio**3)/3

# OUTPUT
print("############################")
print("  FIGURA GEOMETRICA:", cuerpo_geometrico)
print("############################")
print("RADIO=", radio)
print("############################")
print("          VOLUMEN=", volumen)
