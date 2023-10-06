#73. Write a Python program to calculate the midpoints of a line
def getMidpoint(x1,y1,x2,y2):
    mid_x = (x1 + x2)/2
    mid_y = (y1 + y2)/2
    print(f"Midpoint of ({x1},{y2}) and ({x2},{y2}) : ({mid_x},{mid_y})")

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

getMidpoint(x1,x2,y1,y2)