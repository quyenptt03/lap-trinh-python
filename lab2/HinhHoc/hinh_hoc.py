class HinhHoc:
    def __init__(self, cd:float):
        self.canh = cd
    def TinhDienTich(self)->float:
        pass
    def Xuat(self)->str:
        print(f"Dien tich cua hinh co canh {self.canh} la {self.TinhDienTich()}")
    