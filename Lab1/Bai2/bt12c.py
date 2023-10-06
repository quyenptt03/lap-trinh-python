#Tìm số nguyên tố lớn nhất
from math import sqrt
arr = [1,25,2,5,7,3,8,100, 71, 23]

def kt_so_nguyen_to(num:int):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def tim_max_so_nguyen_to(arr):
    kq = -1
    for num in arr:
        if kt_so_nguyen_to(num) and num > kq:
            kq = num
    return kq
if tim_max_so_nguyen_to(arr) == -1:
    print("list khong co chua so nguyen to")
print(tim_max_so_nguyen_to(arr))

