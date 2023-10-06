#10.In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)

def printTriangle(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ') if j == i or j == 0 or i == n - 1 else print(' ', end=' ')
        print()


n = int(input("Nhap n = "))
printTriangle(n)