#Tính trung bình các số lẻ

def Average(lst):
    return sum(lst) / len(lst)

arr = [1,25,2,5,7,3,8,100,2]
new_list = [n for n in arr if n %2 == 1]
avg = Average(new_list)
print("Trung binh cac so le cua mang: ",avg)
