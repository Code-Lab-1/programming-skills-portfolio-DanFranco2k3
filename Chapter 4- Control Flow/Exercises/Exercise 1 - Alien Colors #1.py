#Version that passes
alien_color = 'green'

if alien_color == 'green':
    print("A green alien have taken down, Congratulations! You earned 5 points!")
print()
alien_color = 'red'

if alien_color == 'red':
    print("A red alien have taken down, Congratulations! You earned 5 points!")
print()
alien_color = 'yellow'

if alien_color == 'yellow':
    print("A yellow alien have taken down, Congratulations! You earned 5 points!")
print()

#Version that fails (no output)

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You earned 5 points!")

alien_color = 'yellow'

if alien_color == 'red':
    print("Congratulations! You earned 5 points!")

alien_color = 'green'

if alien_color == 'yellow':
    print("Congratulations! You earned 5 points!")