# Start with some designs that need to be printed.
unprinted_designs = ['phone cases', 'robot pendant', 'dodecahedron']
completed_models = []


# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
def print_models(unrprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


# Display all completed models
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
