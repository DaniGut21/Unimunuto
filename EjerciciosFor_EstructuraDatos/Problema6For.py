# programa que lee 10 numeros y luego muestra cuantos fueron multiplos de 3 y de 5
mul3=0
mul5=0
for f in range(10):
    valor=int(input("Ingrese un valor:"))
    if valor%3==0:
        mul3=mul3+1
    if valor%5==0:
        mul5=mul5+1

print("Cantidad de valores ingresados multiplos de 3:", mul3)
print("Cantidad de valores ingresados multiplos de 5:", mul5)