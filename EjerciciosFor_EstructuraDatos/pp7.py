# programa que realiza la carga de 10 valores enteros y analiza positivos, negarivos, multiplos de 15 y el valor acumulado de los pares
negativos=positivos=multiplos15=0
suma_pares=0
for x in range(10):
    num=int(input("Ingresa el numero:"))
    if num<0:
        negativos+=1
    elif num>0:
        positivos+=1
    if num%15==0:
        multiplos15+=1
    if num%2==0:
        suma_pares+=num 

print("Cantidad de negativos:", negativos)
print("Cantidad de positivos:", positivos) 
print("Cantidad de multiplos de 15:", multiplos15)
print("Suma de pares:", suma_pares)          