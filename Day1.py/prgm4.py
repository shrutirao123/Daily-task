triangle1 = int(input("Enter the first side: "))
triangle2 = int(input("Enter the second side: "))
triangle3 = int(input("Enter the third side: "))

# Calculate the semi-perimeter of the trianglle
side = (triangle1 + triangle2 + triangle3) / 2

#formula to calculate the area of the triangle
area = (side * (side - triangle1) * (side - triangle2) * (side - triangle3)) ** 0.5

## Display the area of the triangle
print("The area of the triangle is:", area)