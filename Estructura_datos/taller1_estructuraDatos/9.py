# 9. Logaritmo entero
def logaritmo_entero(n, base):
    if n < base:
        return 0
    return 1 + logaritmo_entero(n//base, base)

print(logaritmo_entero(64, 2))