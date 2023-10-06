#Xuât tất cả các số lẻ không chia hết cho 5
arr = [1,25,2,5,7,3,8,100]

def kt_so_le_ko_chia_het_5(n:int):
    return n % 5 != 0 and n%2 != 0

new_list = [n for n in arr if kt_so_le_ko_chia_het_5(n)]
new_list2 = filter(kt_so_le_ko_chia_het_5, arr)
print(new_list)

for x in new_list2:
  print(x)