# Write a Python program that converts seconds into hours, minutes, and seconds.
def converseTime(seconds):
    s = seconds
    h = 0
    m = 0
    while s > 60:
        if s > 3600:
            s -= 3600
            h += 1
        elif s > 60:
            s -= 60
            m += 1
    print(f"{seconds} = {h}:{m}:{s}")

seconds = int(input("Enter seconds to converse: "))
converseTime(seconds)