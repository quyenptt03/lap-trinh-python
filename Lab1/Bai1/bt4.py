'''
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
import math

def tinh_dien_tich_hinh_tron(r):
    return math.pi*math.pow(r,2)

r = float(input('Nhap ban kinh: '))
while r <= 0:
    print('Ban kinh vua nhap khong hop le')
    r = float(input('Nhap ban kinh: '))
    
print(f'Dien tich hinh tron ban kinh r = {r} la: {tinh_dien_tich_hinh_tron(r)}')