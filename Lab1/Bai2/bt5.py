#Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
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

n = int(input("Nhap n = "))
print(f"So fibonaci thu {n} la: ", tim_fibo_2(n))