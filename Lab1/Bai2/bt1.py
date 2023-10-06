'''
a) (a + b),
b) a/b,
c) a^b
'''
def sum(a, b):
    return a + b

def div(a,b):
    return a/b

def pow(a, b):
    return a**b

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

print(f"Tong {a}+{b} = ", sum(a,b))
print(f"Thuong {a}/{b} = ", div(a,b))
print(f"Luy thua {a}^{b} = ", pow(a,b))

