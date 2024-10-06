# Step 1: Input the size of the array
size = int(input("Enter the size of the array: "))

# Step 2: Input the elements of the array
elements = list(map(int, input("Enter the elements separated by space: ").split()))

# Check if the number of elements matches the specified size
if len(elements) != size:
    print(f"Error: Expected {size} elements, but got {len(elements)}.")
else:
# Step 3: Display the cube of each element
    for element in elements:
        print(element ** 3)
