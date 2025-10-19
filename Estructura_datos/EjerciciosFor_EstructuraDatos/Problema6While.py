f=0
mul3=0
mul5=0
while f<10:
    valor=int(input("Ingrese un valor:"))
    if valor%3==0:
        mul3=mul3+1
    if valor%5==0:
        mul5=mul5+1
    f=f+1

print("Cantidad de valores ingresados multiplos de 3:", mul3)
print("Cantidad de valores ingresados multiplos de 5:", mul5)