#Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
def tim_fibo(n: int):
    if n <= 1:
        return n
    return tim_fibo(n-1) + tim_fibo(n-2)

def tim_fibo_2(n:int):
    a1 = 1
    a2 = 1
    if n <= 2:
        return 1
    i = 3
    a = 0
    while i <= n:
        a = a1 + a2
        a1 = a2
        a2 = a
        i += 1

    return a

def tong_n_fibo(n:int):
    sum = 0
    for i in range(1, n+1):
        sum += tim_fibo(i)
    return sum

n = int(input("Nhap n = "))
print(f"tong {n} so fibonacci dau tien la: ", tong_n_fibo(n))