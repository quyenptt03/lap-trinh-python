#Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
from math import sqrt
def kt_so_nguyen_to(num:int):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

print("Kiem tra so nguyen to tu a den b ")
a = int(input("a = "))
b = int(input("b = "))

print(f"Danh sach so nguyen to tu {a} den {b}: ")
for i in range(a, b+1):
    if kt_so_nguyen_to(i):
        print(i, end='\t')