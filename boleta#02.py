# recibo de agua
# INPUT
nombre=input("ingrese el nombre:")
dni=input("ingrese el numero de dni:")
residencia=input("ingrese la ciudad donde vive:")
igv=float(input("ingrese el igv:"))
servicio_de_agua=float(input("ingrese el servicio de agua:"))
servicio_de_desague=float(input("ingrese el servicio de desague:"))
cargo_fijo=float(input("ingrese el cargo fijo:"))

# PROCESSING
total_a_pagar= (igv+servicio_de_agua+servicio_de_desague+cargo_fijo)

# OUTPUT
print("#################################################")
print("RECIBO DE AGUA")
print("#################################################")
print("NOMBRE:", nombre, "DNI:", dni)
print("RESIDENCIA:", residencia)
print("#################################################")
print("IGV:", igv)
print("SERVICIO DE AGUA:", servicio_de_agua)
print("SERVICIO DE DESAGUE:", servicio_de_desague)
print("CARGO FIJO:", cargo_fijo)
print("##################################################")
print("TOTAL A PAGAR:", total_a_pagar)