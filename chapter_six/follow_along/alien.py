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
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
"""
# page 106, follow along with the nested dictionarys in a list
""" alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien) """

# create an empty list
aliens = []

# make our 30 elements
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien[color] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# show the frst 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many alien have been created
print(f"Total number of aliens: {len(aliens)}")