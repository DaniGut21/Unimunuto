# programa que solicite 10 numeros e imprima la suma de los ultimos 5 valores
numeros=[]
for x in range(10):
    num=int(input("Ingrese el numero:"))
    numeros.append(num)
    
suma=sum(numeros[-5:]) 
print("La suma de los ultimos 5 numeros es:", suma)   