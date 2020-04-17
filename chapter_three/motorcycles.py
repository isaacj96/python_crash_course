#creating list of motorcycles
motorcycles = ['Honda', 'yamah', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#starting from empty list and then adding each motorcycle to list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#inserting ducati as first mortcycle in list
motorcycles = ['Honda', 'yamah', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
