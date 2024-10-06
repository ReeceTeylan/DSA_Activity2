# Input the side length of the square
side_length = int(input("Enter the side length of the square: "))

# Generate the hollow square
for i in range(side_length):
    if i == 0 or i == side_length - 1:
        print('x' * side_length)
    else:
        print('x' + ' ' * (side_length - 2) + 'x')
