# Accepting input for two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Swapping the numbers
number1, number2 = number2, number1

# Printing the swapped values
print("After swapping the numbers:")
print("First number:", number1)
print("Second number:", number2)