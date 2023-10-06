#Đếm số lần xuất hiện của một số trong danh sách
arr = [1,25,2,5,7,3,8,100,2]

def dem_so_lan_xuat_hien(arr, so):
    count = 0
    for num in arr:
        if num == so:
            count += 1
    return count

print(dem_so_lan_xuat_hien(arr, 1))
