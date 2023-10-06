#68. Write a Python program to calculate sum of digits of a number.
def sum_of_digits(num):
    sum = 0
    numStr = str(num)
    for i in range(len(numStr)):
        sum += int(numStr[i])
    return sum

n = int(input("Enter a number: "))
print(f"Sum of digits of {n} is: ", sum_of_digits(n))