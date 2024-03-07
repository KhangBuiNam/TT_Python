#Tien dien
import os
os.system ('cls')
n = float(input("Nhap vao so kWh dien: "))
SUM = 0
if (n<=100):            #duoi100
    SUM = n*2000
elif (n>100 and n<=200):        #Tu 100-200
    SUM = 100*2000 + (n-100)*4000
elif (n>200):
    SUM = 100*2000 + 100*4000 + (n-200)*9000  #Lon hon 200kwh
print("Tong tien dien la: ",SUM)