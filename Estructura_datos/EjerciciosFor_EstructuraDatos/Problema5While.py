f=0
aprobados=0
reprobados=0
while f<10:
    nota=int(input("Ingrese la nota:"))
    if nota>=7:
        aprobados=aprobados+1
        f=f+1
    else:
        reprobados=reprobados+1 
        f=f+1       

print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)        