# 7. Serie armónica
def serie_armonica(n):
    if n == 1:
        return 1.0
    return 1/n + serie_armonica(n-1)

print(serie_armonica(3))