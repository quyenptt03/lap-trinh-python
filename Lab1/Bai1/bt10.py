#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
def calculate(n):
    return n+n*n+n*n*n

n = int(input("n = "))
print("result: ", calculate(n))