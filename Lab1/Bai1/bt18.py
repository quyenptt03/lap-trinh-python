'''18. Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.'''

def sum_3_nums(a,b,c):
    if a == b and a == c:
        return a * 3 * 3
    else:
        return a + b + c

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("Sum: ", sum_3_nums(a,b,c))