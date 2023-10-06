import math
#8. Giải phương trình bậc 2: ax2 + bx + c=0

def giai_pt_bac_2(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print('phuong trinh vo nghiem')
    elif delta==0:
        x = -b/(2*a)
        print(f'phuong trinh co nghiem kep: x = {x}')
    else:
        square = math.sqrt(delta)
        print(square)
        x1 = (-b+square)/(2*a)
        x2 = (-b-square)/(2*a)
        print(f'phuong trinh co 2 nghiem: x1 = {x1}, x2 = {x2}')

giai_pt_bac_2(3,2,5)
giai_pt_bac_2(4,-2,-6)
giai_pt_bac_2(1,-4,4)