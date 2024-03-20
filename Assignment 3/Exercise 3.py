import os
from math import*
os.system('cls')

class POINT:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f'({self.x}, {self.y})')
    def move(self,m,n):
        self.x = self.x+ m
        self.y = self.y+ n
        print (f'({self.x}, {self.y})')
    def distance(self,b):
        c=b.x
        d=b.y
        s=sqrt((self.x-c)**2 +(self.y-d)**2 )
        print(f'{s}')
        return s

a=POINT(2,3)
b=POINT(5,3)
a.show()
a.move(5,-5)
a.distance(b)