#OOP_Class
import os
import gc                       
os.system('cls')
class CALCULATE:
    def __init__(self):         # ham tao constructor/ tu dong duoc tao
        self.a=0                # 2 bien cua class = 0
        self.b=0
        print ('Constructor is called')
    def __init__(self, a, b):   # Ham tao 2 tham so truyen vao
        print ('Constructor with 2 value param')
        self.a=a                #2 bien cuc bo gan cho 2 bien cua class
        self.b=b

    def sum(self):
        s= self.a + self.b
        return s
    def mul(self, x, y):
        m= x*y
        print ("Mul=" + str(m))
    def __del__(self):          # Ham huy destructor 
        print ('Destructor is called')

t = CALCULATE(2,3)              # thuc hien voi 2 bien class la 2 va 3
t.mul(3,6)                      # a=3 b=6
print ('Sum=' + str(t.sum()))

del t 
gc.collect()                    # Giai phong du lieu
print ('END TASK CALCULATE')
class PEOPLE:
    def __init__(self,name, age, adress):
        self.name = name
        self.age = age
        self.adress= adress
    def printPeopleInfor(self):
        print(f'name: {self.name}, age = {self.age}, adress={self.adress}')
class THPT:
    def __init__(self,math,physical,chemical):
        self.math=math
        self.physical=physical
        self.chemical=chemical
        
class STUDENT(PEOPLE,THPT):                          # CO the ke thua duoc nhieu class
    def __init__(self, stdid, name, avgpoint,age,adress):
        super().__init__(name,age,adress)
        self.stdid= stdid
        self.avgpoint = avgpoint
    def printInfor(self):
        print(f"stdid = {self.stdid}, name = {self.name}, avgpoint = {self.avgpoint}")
    def sumPoint(self, math,physical,chemical ):
        super().__init__(math,chemical,physical)
        s=math + physical+chemical
        print(f'THPTQG = '+str(s))
        return s
    
class LECTURER(PEOPLE):
    def __init__(self, ltrid:str, name:str, wage:str, age:int, adress:str):
        super().__init__(name, age, adress)
        self.ltrid=ltrid
        self.wage= wage
    def ltrInfor(self):
        print(f"ltrid = {self.ltrid}, name = {self.name}, wage = {self.wage}")                  # TRUNG NHAU NHIEU BIEN NEN CAN 1 CLASS KE THUA CHI CAN KHAI BAO 1 LAN
        print (f'age= {self.age}, adress= {self.adress}')
        super().printPeopleInfor()

sv = STUDENT("22139029", 'Bui Nam Khang', 6.5, 19, "HCM")
sv.printInfor()
sv.sumPoint(8,9,10)
ltr = LECTURER("07119014","Huynh Hoang Ha", '2.000 USD', 30, "Vung Tau")
ltr.ltrInfor()
