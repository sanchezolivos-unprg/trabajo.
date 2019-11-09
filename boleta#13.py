# UTILES ESCOLARES
# INPUT
alumno=input("ingrese el nombre del alumno:")
precio1=float(input("ingrese el precio de 5 cuadernos:"))
precio2=float(input("ingrese el precio de 10 lapices:"))
precio3=float(input("ingrese el precio de 10 lapiceros:"))
precio4=float(input("ingrese el precio de 6 libros:"))
precio5=float(input("ingrese el precio de 2 pegamentos:"))
precio6=float(input("ingrese el precio de 1 mochila:"))

# PRCESSING
total= (precio1+precio2+precio3+precio4+precio5+precio6)

# OUTPUT
print("               boleta de pago                      ")
print("###################################################")
print("5 cuadernos=", precio1,      "10 lapices=", precio2)
print("10 lapiceros=", precio3,      "6 libros=", precio4 )
print("2 pegamentos=", precio5,       "1 mochila=", precio6)
print("###################################################")
print("toal a pagar=", total)