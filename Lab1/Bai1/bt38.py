'''
38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''
def identity(x,y):
    return x**2 + 2*x*y + y**2

a = float(input("a = "))
b = float(input("b = "))

print(f"({a}+{b})^2 = {identity(a,b)}")