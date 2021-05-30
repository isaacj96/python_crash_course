def ingredients(*item):
    print("Pizza will have the following topings: ")
    for topping in item:
        print(f"- {topping}")


ingredients("Pepperoni")
ingredients("Sausage", "Pepperoni", "Meatballs")
ingredients("Ham", "Pineapple")
