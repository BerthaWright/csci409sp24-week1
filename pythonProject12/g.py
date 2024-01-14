class car:
    features=["AC", "Power Steering"]
    def __init__(self,car_make,car_model="M3",rate=4):
        self.make=car_make
        self.model=car_model
        self.rating=rate

    def __str__(self):
        return "The car is a "+ self.make + " "+self.model

    def __add__(self, other):
        return self.rating + other


my_car = car("Astin Martin",car_model="DB5",rate=20)
your_car = car("BMW", car_model="i5")
other_car = car("Chevy")
print(my_car)
print(your_car)
print(other_car)
print(my_car+your_car)
