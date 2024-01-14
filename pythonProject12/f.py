class car:
    def __init__(self):
        self.make="BMW"
        self.model="M3"


print(car)
my_car = car()
print(my_car)
print(type(my_car))

print(my_car.make)
print(my_car.model)

my_car.make = "Ford"
my_car.model = "F-150"
print(my_car.make)
print(my_car.model)
