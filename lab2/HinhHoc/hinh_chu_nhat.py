from hinh_hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, cd: float, cr: float):
        super().__init__(cd)
        self.cr = cr
    
    @property
    def ChieuDai(self):
        return self.canh if self.canh > self.cr else self.cr
    @property
    def ChieuRong(self):
        return self.canh if self.canh < self.cr else self.cr
    
    def TinhDienTich(self) -> float:
        return self.ChieuDai * self.ChieuRong

    def Xuat(self) -> str:
        print(f"Hinh chu nhat co chieu dai {self.ChieuDai}, chieu rong {self.ChieuRong} co dien tich la: {self.TinhDienTich()}")