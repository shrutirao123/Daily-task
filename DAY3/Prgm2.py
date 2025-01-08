# Accepting inputs from user
number1 = int(input("Enter the first number: "))  
number2 = int(input("Enter the second number: "))  
number3 = int(input("Enter the third number: ")) 

# Find the largest number
if number1 >= number2 and number1 >= number3:
    largest = num1  # number1 is the largest
elif number2 >= number1 and number2 >= number3:
    largest = number2  # number2 is the largest
else:
    largest = number3  # number3 is the largest

# Output the largest number
print("The largest number is:", largest)
