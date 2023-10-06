from hinh_hoc import HinhHoc
import sys
from loai_hinh import LoaiHinh
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from hinh_chu_nhat import HinhChuNhat

class DanhSachHinhHoc():
    def __init__(self) -> None:
        self.ds = []

    def themHinh(self, hh: HinhHoc):
        self.ds.append(hh)
    
    def xuat(self):
        for hh in self.ds:
            hh = HinhHoc(hh)
            hh.Xuat()

    def timDTMax(self):
        max = -1
        for hinh in self.ds:
            hinh = HinhHoc(hinh)
            if (hinh.TinhDienTich() > max):
                max = hinh.TinhDienTich()
        return max
    
    def timDTMin(self):
        min = sys.maxsize
        for hinh in self.ds:
            hinh = HinhHoc(hinh)
            if (hinh.TinhDienTich() < min):
                min = hinh.TinhDienTich()
        return min
    
    def timHinhCoDienTichLonNhat(self):
        kq = DanhSachHinhHoc()
        dtmax = self.timDTMax()
        for hinh in self.ds:
            hinh = HinhHoc(hinh)
            if hinh.TinhDienTich() == dtmax:
                kq.ds.append(hinh)
        
        return kq

    def TimHinhCoDienTichNhoNhat(self):
        kq = DanhSachHinhHoc()
        dtmin = self.timDTMin()
        for hinh in self.ds:
            hinh = HinhHoc(hinh)
            if hinh.TinhDienTich() == dtmin:
                kq.ds.append(hinh)
        
        return kq
    def TimHinhTronNhoNhat(self):
        pass
    def SapGiamTheoDT(self):
        return self.ds.sort(key=lambda x: x.dienTich, reverse=True)
    def DemSoLuongHinh(self, loai: LoaiHinh):
        result = []
        if (loai == LoaiHinh.HinhTron):
            result = [hh for hh in self.ds if isinstance(hh, HinhTron)]
        elif (loai == LoaiHinh.HinhVuong):
            result = [hh for hh in self.ds if isinstance(hh, HinhVuong)]
        elif (loai == LoaiHinh.HinhChuNhat):
            result = [hh for hh in self.ds if isinstance(hh, HinhChuNhat)]
        return f"Co {len(result)} {loai}"
    def TinhTongDT(self):
        sum = 0
        for hh in self.ds:
            hh = HinhHoc(hh)
            sum += hh.TinhDienTich()
        return sum
    def TimHinhCoDTLonNhat(kieu: LoaiHinh):
        pass
    def TimViTriCuaHinh(self, h: HinhHoc):
        for hh in self.ds:
            if (isinstance(hh, h) and hh.canh == h.canh):
                return hh
    def TimHinhTheoDTich(self, dt: float):
        return [hh for hh in self.ds if (hh.dienTich == dt)]
    def XoaHinh(self, hh: HinhHoc):
        self.ds.remove(hh)
    


    