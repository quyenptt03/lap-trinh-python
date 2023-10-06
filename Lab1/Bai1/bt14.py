'''14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''
from datetime import date
def calculate_dates_between(dt1, dt2):
    d = dt2 - dt1
    return d.days

print("Enter date 1: ")
d1 = int(input("d1 = "))
m1 = int(input("m1 = "))
y1 = int(input("y1 = "))
d1 = date(y1,m1,d1)

print("Enter date 2: ")
d2 = int(input("d2 = "))
m2 = int(input("m2 = "))
y2 = int(input("y2 = "))
d2 = date(y2,m2,d2)

print(f"Number of days between {d1} and {d2} is: ", calculate_dates_between(d1,d2))