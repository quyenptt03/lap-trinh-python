def tinhtb(ds):
    ds = list(ds)
    print(ds)
    sum = 0
    for n in ds:
        sum += n
    return sum/len(ds)
    
arr = []
while(True):
    try:
        n = float(input("Nhap n: "))

    except:
        print("So nhap vao khong hop le")
        break
    arr.append(n)

print(tinhtb(arr))