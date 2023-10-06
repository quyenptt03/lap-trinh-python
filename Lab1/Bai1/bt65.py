#65. Write a Python program that converts seconds into days, hours, minutes, and seconds.
def converseTime(seconds):
    s = seconds
    d = 0
    h = 0
    m = 0
    while s > 60:
        if s > 86400:
            s -= 86400
            d += 1
        elif s > 3600:
            s -= 3600
            h += 1
        elif s > 60:
            s -= 60
            m += 1
    print(f"{seconds} = {d} day(s) - {h} hour(s) - {m} minute(s) - {s} second(s)")

seconds = int(input("Enter seconds to converse: "))
converseTime(seconds)