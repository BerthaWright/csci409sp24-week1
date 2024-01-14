class car:
    features=["AC", "Power Steering"]
    def __init__(self, car_make, car_model="M3"):
        self.make=car_make
        self.model=car_model


my_car = car("Astin Martin",car_model="DB5")
your_car = car("BMW", car_model="i5")
other_car = car("Chevy")
print(my_car.make)
print(my_car.model)
print(your_car.make)
print(your_car.model)
print(other_car.make)
print(other_car.model)