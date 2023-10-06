#Xuất tất cả các số Fibonacci
import math

arr = [1,25,2,5,7,3,8,100]

def check_perfect_square (m):
    n = int (math.sqrt (m))
    return n * n == m 

def check_fibo (m ): 
    return check_perfect_square (5 * m * m + 4) or check_perfect_square (5 * m * m - 4)

for num in arr:
    if check_fibo(num):
        print(num, end='\t')
