""" alien_0={'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) """

# if we ignore the code above this line, and just use the code below the line, we'll be adding to an empty dictionary which is sometimes "convienent" or "necessary"
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# alien_0['color'] = 'yellow'
# print(alien_0)

""" alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right,
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a face alien.
    x_increment: 3

#The new position is the old position plus the new increment.
alien_0['x_position'] += x_increment
print(f"The new position is: {alien_0['x_position']}") """

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
