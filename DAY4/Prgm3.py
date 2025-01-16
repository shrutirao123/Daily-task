# Taking 5 numbers as input from the user in a single line
numbers = list(map(int, input("Enter 5 numbers separated by spaces: ").split()))

# Find and display the maximum and minimum
print("The maximum number is:", max(numbers))
print("The minimum number is:", min(numbers))
