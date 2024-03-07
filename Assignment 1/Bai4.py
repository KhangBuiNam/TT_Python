#Bang cuu chuong
import os
os.system("cls")
n = int(input("Nhap mot so nguyen duong bat ky: "))
for i in range(1,11):
    print(str(n)+" * "+str(i)+" = "+str(n*i))