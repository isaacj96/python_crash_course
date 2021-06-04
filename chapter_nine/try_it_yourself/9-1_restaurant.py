class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and it's a "
              f"{self.type.title()} type of restaurant.")

    def open_restaurant(self):
        print("The restaurant is open!")


my_rest = Restaurant("Pizzeria", "Italian")
print(my_rest.name)
print(my_rest.type)

my_rest.describe_restaurant()
my_rest.open_restaurant()
