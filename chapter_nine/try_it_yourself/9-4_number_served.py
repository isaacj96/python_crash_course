class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and it's a "
              f"{self.type.title()} type of restaurant.")

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, amount):
        self.number_served += amount


my_rest = Restaurant("Pizzeria", "Italian")
print(my_rest.name)
print(my_rest.type)

my_rest.describe_restaurant()
my_rest.open_restaurant()

print(my_rest.number_served)
my_rest.number_served = 10
print(my_rest.number_served)

my_rest.set_number_served(5)
print(my_rest.number_served)

my_rest.increment_number_served(10)
print(my_rest.number_served)
