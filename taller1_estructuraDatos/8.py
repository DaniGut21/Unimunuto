# 8. Decimal a binario
def decimal_a_binario(n):
    if n <= 1:
        return str(n)
    return decimal_a_binario(n//2) + str(n % 2)

print(decimal_a_binario(10))