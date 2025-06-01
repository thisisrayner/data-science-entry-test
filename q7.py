class Car:
    """
    Car class with make, model, year.
    Can print itself as "Year Make Model"
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # print out the car details in the required format
        print(f"{self.year} {self.make} {self.model}")

# create a Car object (instance) with the given details
my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()  # should print: 2020 Toyota Corolla
