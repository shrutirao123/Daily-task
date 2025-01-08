# Input the distance traveled
distance = int(input("Enter the distance traveled (in kilometers): "))

# Calculate fare based on the distance
if 1 <= distance <= 50:
    fare = distance * 8  # 8 Rs. per km for 1-50 km
elif 51 <= distance <= 100:
    fare = distance * 10  # 10 Rs. per km for 51-100 km
elif distance > 100:
    fare = distance * 12  # 12 Rs. per km for more than 100 km
else:
    fare = 0  # Invalid distance (less than 1 km)

# Output the calculated fare
print("The fare is: Rs.", fare)
