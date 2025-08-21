# 3. Producto de dos números
def producto(a, b):
    if b == 0:
        return 0
    return a + producto(a, b-1)

print(producto(3, 4)) 