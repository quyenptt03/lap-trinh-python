#40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
import math
def calDistance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))

print(calDistance(1,2,5,3))