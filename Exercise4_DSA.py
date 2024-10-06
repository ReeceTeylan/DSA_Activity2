# Input the height of the triangle
height = int(input("Enter the height of the triangle: "))

# Loop to create the inverted triangle
for i in range(height, 0, -1):
    print('*' * i)
