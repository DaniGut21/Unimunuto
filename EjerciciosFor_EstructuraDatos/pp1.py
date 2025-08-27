# programa que lee n pares de datos, cada par corresponde a la medida de la base y altura de un triangulo
n=int(input("Cuantos triangulos va a ingresar?:"))
mayores12=0
for x in range(n):
    base=int(input("ingresa la base:"))
    altura=int(input("ingresa la altura:"))
    area=int((base*altura)/2)
    if area>12:
        mayores12+=1
    print("Base:", base, "Altura:", altura, "Area:", area)    
    
print("La cantidad de triangulos con area mayor a 12 son:", mayores12)        