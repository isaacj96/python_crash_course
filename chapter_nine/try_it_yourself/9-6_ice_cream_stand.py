class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and it's a "
              f"{self.type.title()} type of restaurant.")

    def open_restaurant(self):
        print("The restaurant is open!")


class IceCreamStand(Restaurant):
    def __init__(self, name, type='Ice Cream'):
        super().__init__(name, type)
        self.flavors = ['Chocolate', 'Vanilla', 'Cookies n Cream']

    def display_flavor(self):
        for flavor in self.flavors:
            print(flavor)


iceCream = IceCreamStand("Isaac's Ice Cream Stand")
iceCream.flavors = ['Banana', 'Cookie Dough', 'Strawberry']

iceCream.describe_restaurant()
iceCream.display_flavor()
