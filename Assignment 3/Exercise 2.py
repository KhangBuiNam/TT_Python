import os
os.system('cls')
class VEHICLE:
    def __init__(self,max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def printInfor(self):
        print(f'Max speed is : {self.max_speed}, \nMileage is : {self.mileage} dam/km')
class BUS(VEHICLE):
    def __init__(self,color:str, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.color= color
    def showBusInfo(self):
        print(f'Color is: {self.color} \nMax speed is : {self.max_speed} \nMileage is: {self.mileage} dam/km')

if __name__== '__main__':
    vehicle=BUS("Blue" ,20,30)
    vehicle.showBusInfo()