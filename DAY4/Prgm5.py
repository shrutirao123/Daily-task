# Lambda function to check if the number is positive, negative, or zero
check_number = lambda number: 'Positive' if number > 0 else 'Negative' if number < 0 else 'Zero'

# Taking input from the user
number = float(input("Enter a number: "))

# Display the result based on the input
print(check_number(number))
