# ejercicio practico 8
def promedio_estudiantes(cantidad, turno):
    suma=0
    for x in range(cantidad):
        edad=int(input("Ingrese la edad del estudiante:"))
        suma+=edad
    return suma/cantidad

prom_dia=promedio_estudiantes(5, "mañana")
prom_tarde=promedio_estudiantes(6, "tarde")
prom_noche=promedio_estudiantes(11, "noche")

print("Promedio mañana:", prom_dia)
print("Promedio tarde:", prom_tarde)
print("Promedio noche:", prom_noche)

if prom_dia>prom_tarde and prom_dia>prom_noche:
    print("El turno de la mañana tiene el mayor promedio de edades")
elif prom_tarde>prom_noche:
    print("El turno de la tarde tiene el mayor promedio de edades")
else:
    print("El turno de la noche tiene el mayor promedio de edades")