# We're now working with examples that are omplex enough that they can be extended in any number of ways. Use one of the example programs from this chapter and extend it by adding
# new keys and values, changing the context of the program or improving the formatiing of the output.

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
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# show the frst 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

for alien in aliens[3:8]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] ='fast'

for alien in aliens[:10]:
    print(alien)
print("...")

# Show how many alien have been created
print(f"Total number of aliens: {len(aliens)}")