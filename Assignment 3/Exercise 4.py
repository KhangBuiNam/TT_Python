import os
os.system('cls')

class RECTANGLE:
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def Perimeter(self):
        c= (self.length + self.width)*2
        print(f'Perimeter: {c}')
        return c

    def Area(self):
        s= self.length*self.width
        print(f'Area: {s}')
        return s
    def display(self):
        print('Rectangle have : ')
        print(f'Length is: {self.length}')
        print(f'Width is : {self.width}')
        self.Area()
        self.Perimeter()
class RectangleVolume(RECTANGLE):
    def __init__(self,height, length, width):
        super().__init__(length, width)
        self.height = height
    def Volume(self):
        v=(self.length*self.width)*self.height
        print(f'\nVolume = {v}')
    def display(self):
        print(f'Height is: {self.height}')
        super().display()
if __name__=="__main__":
    hcn= RECTANGLE(3,4)
    hcn.display()
    vhcn=RectangleVolume(3,4,5)
    vhcn.display()
    vhcn.Volume()
   