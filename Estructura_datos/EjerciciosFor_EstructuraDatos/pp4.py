# programa que permita ingresar un valor del 1 al 10 y muestre la tabla de multiplicar del mismo
num=int(input("Ingresa un numero del 1 al 10:"))
for x in range(1,13):
    print(num, "x", x, "=", (num*x))