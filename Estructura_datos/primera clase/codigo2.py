#ingresar 3 variables y decir cual es la mayor
a=int(input("ingresa valor A"))
b=int(input("ingresa valor B"))
c=int(input("ingresa valor C"))
if a>b:
  if a>c:
    print(a, "es el mayor")
  else:
    print(c, "es el mayor")
else:
  if b>c:
    print(b, "es el mayor")
  else:
    print(c, "es el mayor")