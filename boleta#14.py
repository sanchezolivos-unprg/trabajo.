# RECIBO DE LUZ
# INPUT
nombre=input("ingrese el nombre:")
num_dni=input("ingrese el numero de DNI:")
edad=int(input("ingrese la edad del dueño:"))
fecha_emision=str(input("ingrese la fecha de emision:"))
potencia=float(input("ingrese la potencia en kw:"))
consumo=float(input("ingrese el consumo en kwh:"))
interes_monatorio=float(input("ingrese el interes monatorio:"))
cargo_fijo=float(input("ingrese el cargo figo:"))

# PROCESSING
total= (potencia+consumo+interes_monatorio+cargo_fijo)

# OUTPUT
print("######################################")
print("            RECIBO DE LUZ             ")
print("######################################")
print("fecha de emision:", fecha_emision)
print("nombre:", nombre,        "DNI:", num_dni)
print("edad:", edad)
print("fecha de emision:", fecha_emision)
print("######################################")
print("potencia en kw=", potencia)
print("consumo=", consumo)
print("interes monatorio=", interes_monatorio)
print("cargo fijo=", cargo_fijo)
print("######################################")
print("total a pagar=", total)