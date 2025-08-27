# Programa que solicita 10 notas de alumnos e informa cuantos tienen notas mayores o iguales a 7 y cuantos menores
aprobados=0
reprobados=0
for f in range(10):
    nota=int(input("ingrese la nota:"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1

print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)