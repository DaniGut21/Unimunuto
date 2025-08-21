# 6. Invertir secuencia
def invertir_secuencia(sec):
    if len(sec) == 0:
        return ""
    return invertir_secuencia(sec[1:]) + sec[0]

print(invertir_secuencia("Hola"))