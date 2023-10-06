# 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

def cal_diff_17(n):
    return (n-17)*2 if n>17 else 17-n

n = float(input("Enter a number: "))
print(f"The difference between 17 and {n} is: ", cal_diff_17(n))