def div(number1, number2): 
    if number2 == 0: 
        return "Cannot divide by zero"
    return number1 / number2 

# Taking inputs from the user
number1 = float(input("Enter the numerator: "))  # Input numerator
number2 = float(input("Enter the denominator: "))  # Input denominator

# Displaying the result
print("The result of the division is:", div(number1, number2))
