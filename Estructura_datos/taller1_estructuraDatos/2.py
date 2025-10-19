# 2. Suma hasta número positivo
def suma_hasta(n):
    if n <= 0:
        return 0
    return n + suma_hasta(n-1)

print(suma_hasta(5)) 