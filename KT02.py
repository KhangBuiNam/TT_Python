import os
os.system('cls')

class NGUOI:
    def __init__(self,ten,cccd):
        self.ten = ten
        self.cccd= cccd

class NHANVIEN (NGUOI):
    def __init__(self, ten, cccd, maNV , luong=float):
        super().__init__(ten, cccd)
        self.maNV= maNV
        self.luong = luong

class nhansu:
    def __init__(self):
        self.SL = int(input('Nhap so luong nhan vien: '))
        self.DS_nhanvien = []

    def printInfor(self):                                             #Function 1 
        for i in range(self.SL):
            ten= str(input('Nhap ten nhan vien: '))
            cccd= str(input('Nhap cccd: '))
            maNV= str(input('Nhap ma nhan vien: '))
            luong= float(input('Nhap luong: '))
            self.DS_nhanvien.append(NHANVIEN(ten,cccd,maNV, luong))
            self.max_luong= self.DS_nhanvien[0].luong
            self.min_luong= self.DS_nhanvien[0].luong
            self.max_luongInfor= self.DS_nhanvien[0]
            self.min_luongInfor= self.DS_nhanvien[0]

    def display(self):                                                #Function 2
        print('Danh sach nhan vien: ')
        for k in self.DS_nhanvien: 
            print(f'{k.ten}, {k.cccd}, {k.maNV}, {k.luong}')

    def luong_giam(self):                                             #Function 3
        print('DS giam dan theo luong: ')
        luong_reduce= sorted(self.DS_nhanvien, key=lambda x:x.luong, reverse=True)
        for i, k in enumerate(luong_reduce):
            print(f'{k.ten}, {k.luong}')
    def min_max_luong(self):                                         #Function 4
        luong_min= min(self.DS_nhanvien, key=lambda x:x.luong)
        luong_max= max(self.DS_nhanvien, key=lambda x:x.luong)
        for i in self.DS_nhanvien:
            if i.luong == luong_max.luong:
                self.max_luongInfor = i
                print (f'Nhan vien co luong cao nhat: {self.max_luongInfor.ten}:  {self.max_luongInfor.luong}')
        for i in self.DS_nhanvien:
            if i.luong == luong_min.luong:
                self.min_luongInfor = luong_min
                print (f'Nhan vien co luong thap nhat: {self.min_luongInfor.ten} : {self.min_luongInfor.luong}')

if __name__== '__main__':
    nv=nhansu()
    nv.printInfor()
    nv.display()
    nv.luong_giam()
    nv.min_max_luong()