class Car: 
    
    def __init__(self,model,make,color,year):
        self.make= make
        self.model= model
        self.year= year
        self.color= color


    def drive(self):
        print(f"This car: {self.model} driving")

    def stop(self):
        print(f"This car: {self.model} is stopped")




car_1 = Car("Chevy","Corvette",2021,'Blue') 
car_2= Car("Ford","Mustang",2022,"Red")

car_1.drive()
car_2.stop()   




