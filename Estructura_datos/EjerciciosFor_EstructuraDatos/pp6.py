# programa que pide ingresar cordenadas (x,y) que representan puntos en un plano
n=int(input("Cuantos puntos vas a ingresar?:"))
for i in range(n):
    x=int(input("Ingresa el punto x:"))
    y=int(input("Ingresa el punto y:"))
    
    if x>0 and y>0:
        print("Primer cuadrante")
    elif x<0 and y>0:
        print("Segundo cuadrante")
    elif x<0 and y<0:
        print("Tercer cuadrante")
    elif x>0 and y<0:
        print("Cuarto cuadrante")
    else:
        print("Esta sobre un eje")