#Make a list called sandwich_orders
sandwich_orders = ['Ham and Cheese', 'Turkey and Cheese', 'tuna', 'california club', 'pastrami', 'pastrami', 'pastrami']

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
#Make a list called finished_sandwiches
finished_orders = []

while sandwich_orders:
    transition_orders = sandwich_orders.pop()

    finished_orders.append(transition_orders)

    for sandwich in finished_orders:
        print(f"I made your {sandwich.title()} sandwich")