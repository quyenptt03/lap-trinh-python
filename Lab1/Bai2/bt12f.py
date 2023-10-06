#Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
arr = [1,25,2,5,7,3,8,100,2]

def kt_so_le_ko_chia_het_3(n:int):
    return n % 3 != 0 and n%2 != 0

new_list= [ n for n in arr if kt_so_le_ko_chia_het_3(n)]

def tich(arr):
    kq = 1
    for n in arr:
        kq *= n
    return kq

print(tich(new_list))
