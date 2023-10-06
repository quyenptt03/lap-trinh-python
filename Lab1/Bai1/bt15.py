#Write a Python program to get the volume of a sphere with radius six.
import math

def calculate_volumn_sphere(r):
    return 4/3 * math.pi * math.pow(r,3)


r = float(input("r = "))
if(r <= 0):
    r = float(input("r = "))

print(f"volumn of a sphere r = {r} is {calculate_volumn_sphere(r)}")
