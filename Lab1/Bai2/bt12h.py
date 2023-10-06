#Đảo ngược trật tự các phần tử của danh sách
arr = [1,25,2,5,7,3,8,100,2]

def dao_nguoc(list):
    start = 0
    end = len(arr) -1
    while start < end:
        tam = list[start]
        list[start] = list[end]
        list[end] = tam
        
        start += 1
        end -= 1


print("mang truoc khi dao nguoc: ", arr)
dao_nguoc(arr)
print("mang sau khi dao nguoc: ", arr)
