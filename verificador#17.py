# verificador al calculadora 17
fisica= "electrostatica"
constante_de_coulomb= 9000000000
carga1= 0.000004
carga2= 0.0000006
distancia= 3
fuerza_electrica= constante_de_coulomb*carga1*carga2/(distancia**2)

print("calculo de la fuerza electrica")
print("la ley de coulomb es:", constante_de_coulomb)
print("la carga 1 es:", carga1)
print("la carga 2 es:", carga2)
print("la distancia es:", distancia)

# verificador
la_fuerza= (fuerza_electrica==0.0024)
print("la fueza electrica es 0.0024:", la_fuerza)