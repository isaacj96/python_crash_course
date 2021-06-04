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
my_sec = Restaurant("Chipotle", "Mexican")
my_thurd = Restaurant("McDonald's", "American")

my_rest.describe_restaurant()
my_sec.describe_restaurant()
my_thurd.describe_restaurant()
