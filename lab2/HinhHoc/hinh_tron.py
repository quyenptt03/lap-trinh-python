from hinh_hoc import HinhHoc
import math

class HinhTron(HinhHoc):
    def __init__(self, bk: float):
        super().__init__(bk)

    @property
    def banKinh(self):
        return self.canh
    
    def TinhDienTich(self) -> float:
        return math.pi * math.pow(self.banKinh,2)
    