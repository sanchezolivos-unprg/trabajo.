# venta de celulares
print("venta de celulares")
cel1=float(input("ingrese el precio del telefono samsumg:"))
cel2=float(input("ingrese el precio del telefono huawei:"))
cel3=float(input("inggrese el precio del telefono motorola:"))
cantidad_de_cel=int(input("ingrese la cantidad de celulares:"))

# PROCESSING
promedio= (cel1+cel2+cel3)/cantidad_de_cel

# OUTPUT
print("###########################################")
print("          VENTA DE CELULARES               ")
print("###########################################")
print("CELULAR SAMSUMG=", cel1)
print("CELULAR HUAWEI=", cel2)
print("CELULAR MOTOROLA=", cel3)
print("###########################################")
print("TOTAL=", promedio)