'''9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''
print("enter the exam test date: ")
d = int(input("d = "))
m = int(input("m = "))
y = int(input("y = "))

print(f"The examination will start from : {d} / {m} / {y}")