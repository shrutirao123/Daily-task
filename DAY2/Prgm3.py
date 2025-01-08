# Conversion factor: 1 kilometer is approximately 0.621371 miles
conversion_factor = 0.621371

# Input from the user
kilometers = int(input("Enter distance in kilometers: "))

# Convert kilometers to miles
miles = kilometers * conversion_factor

print(str(kilometers) + " kilometers is equal to " + str(round(miles)) + " miles.")# Using string concatenation for the output also It converts numbers to strings and adding them to the sentence
