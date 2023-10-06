#Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ
def doi_cho_mang(arr, i,j):
    if i >= len(arr) or j >= len(arr) or i <= -len(arr) or j <= -len(arr):
        print('i hoac j ko hop le')
        return
    arr[i],arr[j] = arr[j], arr[i]

arr = [1,25,2,5,7,3,8,100,2]
i = int(input("Nhap vi tri i = "))
j = int(input("Nhap vi tri j = "))

print(f"Mang truoc khi doi cho vi tri {i} va {j}: ")
print(arr)

doi_cho_mang(arr,i,j)

print(f"Mang sau khi doi cho vi tri {i} va {j}: ")
print(arr)
