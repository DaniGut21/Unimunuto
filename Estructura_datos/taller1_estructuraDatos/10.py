# 10. Contar dígitos
def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n//10)

print(contar_digitos(12345))