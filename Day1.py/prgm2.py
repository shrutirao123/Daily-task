#Accepting inputs from users 
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))

# conditional expression to find the largest number 
Number=number1 if number1>number2 else number2

# Display the largest number
print("The Largest Number is: ",Number)