# Recursive function to calculate power
def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent - 1)

# Input the base and exponent from the user
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Output the result of base raised to the power of exponent
print(f"{base}^{exponent} = {power(base, exponent)}")
