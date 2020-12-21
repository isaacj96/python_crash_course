# Turn your if else chain from 5-4 into an if-elif-else chain
alien_color = ['green', 'yellow', 'red']

alien_color = 'green'
if 'green' in alien_color:
    print("You just earned 5 points for killing the alien")

elif 'yellow' in alien_color:
    print("You just earned 10 points!")

else:
    print("You just earned 15 points!")
