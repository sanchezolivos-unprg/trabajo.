# BOLETA DE PAGO
# INPUT
restaurante= input("ingrese el nombre del restaurante:")
asistente=input("ingrese el nombre del asistente:")
consumidor=input("ingrese el nombre del consumidor:")
plato1= str(input("ingrese el nombre del plato 1:"))
plato2= str(input("ingrese el nombre del plato 2:"))
precio_jugo= float(input("ingrese el precio del jugo:"))
precio1= float(input("igrese el precio del plato 1:"))
precio2=float(input("ingrese el precio el plato 2:"))

# PROCESSING
total= (precio1+precio2+precio_jugo)

# OUTPUT
print("##########################################")
print("        RESTAURANTE:", restaurante         )
print("##########################################")
print("ASISTENTE:", asistente)
print("##########################################")
print("CONSUMIDOR=", consumidor)
print("##########################################")
print("PLATO 1=", plato1,      "PLATO 2=", plato2)
print("##########################################")
print("precio del jugo=", precio_jugo)
print("precio del plato 1=", precio1)
print("precio del plato 2=", precio2)
print("##########################################")
print("total a pagar=", total)