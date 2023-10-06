'''34. Write a Python program to sum two given integers. 
However, if the sum is between 15 and 20 it will return 20.'''
def sum_2_int(a,b):
    if (a+b) >=15 and (a+b) <= 20:
        return 20
    return a+b

a = int(input("Enter a = "))
b = int(input("Enter b = "))

print(sum_2_int(a,b))