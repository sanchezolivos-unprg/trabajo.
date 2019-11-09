# DATOS DEL ESTUDIANTE
# INPUT
estudiante=input("ingrese el nombre del estudiante:")
numero_de_telefono=input("ingrese el numero telefonico:")
peso=int(input("ingrese el peso del estudiante:"))
haltura=float(input("ingrese la haltura del estudiante:"))

# PROCESSING
mc= (peso*haltura)/2

# OUTPUT
print("###################################################################")
print("# DATOS DEL ESTUDIANTE")
print("###################################################################")
print("nombre:", estudiante ,"      numero de telefono:",numero_de_telefono)
print("peso:", peso , "             haltura:", haltura)
print("###################################################################")
print("su masa corporal del estudiante es:", mc)
