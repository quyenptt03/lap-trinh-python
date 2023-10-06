from hinh_chu_nhat import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float):
        super().__init__(canh, canh)

    def Xuat(self) -> str:
        print(f"Hinh vuong co canh {self.canh} co dien tich la {self.TinhDienTich()}")