#Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
import math

def check_perfect_square (m):
    n = int (math.sqrt (m))
    return n * n == m 

def check_fibo (m ): 
    return check_perfect_square (5 * m * m + 4) or check_perfect_square (5 * m * m - 4)

n = int (input ("Vui lòng nhập giá trị nguyên để kiểm tra số Fibonacci:"))

if (check_fibo (n)): 
    print (n, "là số Fibonacci") 
else:
    print (n , "không phải là số Fibnacci")