'''11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.'''
import math
n = float(input("Enter a number: "))
print(f"abs({n}) = {math.fabs(n)}")