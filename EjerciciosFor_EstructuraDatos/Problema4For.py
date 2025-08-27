# Programa que permite ingresar 10 valores y posteriormente mostrar la suma y promedio de ellos
suma=0
for f in range(10):
    valor=int(input("Ingrese valor:"))
    suma=suma+valor

print("La suma es:", suma)
promedio=suma/10
print("El promedioo es:", promedio)