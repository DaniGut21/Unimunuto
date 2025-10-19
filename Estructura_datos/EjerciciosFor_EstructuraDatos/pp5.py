# programa que lee los lados de n triangulos e informa su tipo y cantidad de triangulos de cada tipo
n=int(input("cuantos triangulos vas a ingresar?:"))
equilatero=isosceles=escaleno=0
for x in range(n):
    l1=int(input("lado 1 del triangulo:"))
    l2=int(input("lado 2 del triangulo:"))
    l3=int(input("lado 3 del triangulo:"))

    if l1==l2==l3:
        equilatero+=1
    elif l1==l2 or l1==l3 or l2==l3:
        isosceles+=1
    else:
        escaleno+=1

print("Equilateros:", equilatero)
print("Isosceles:", isosceles)
print("Escalenos:", escaleno)            