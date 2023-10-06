# Tính n!
def tinh_giai_thua(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(tinh_giai_thua(5))
print(tinh_giai_thua(10))
print(tinh_giai_thua(3))