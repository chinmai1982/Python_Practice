class Vehicle:

    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("This is a Vehicle")
        print("The mileage of the Vehicle is : " ,self.mileage)
        print("The cost of the Vehicle is : " ,self.cost)


class Car(Vehicle):

    def __init__(self, mileage, cost,tyres,hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp


    def show_car_details(self):
        print("This is a car")
        print("The number of tyres are : ",self.tyres)
        print("The Value of horse power is :",self.hp)



c1 = Car(200,60984,4,300)   
c1.show_details()
c1.show_car_details()
           