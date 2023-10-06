#Tính tổng căn bậc 2 của n số nguyên đầu tiên
import math
def TongCanBac2(n: int):
    result = 0
    for i in range(1, n+1):
        result += math.sqrt(i)

    return result


n = int(input("Nhap so n: "))
print(f"Tong can bac 2 cua {n} so nguyen dau tien la: ", TongCanBac2(n))
