# Accepting product code and order amount
product_code = int(input("Enter product code (1 for Battery Based, 2 for Key-Based, 3 for Electrical Charging Based): "))
order_amount = int(input("Enter order amount (Rs.): "))

# Apply discounts based on product code and order amount
if product_code == 1 and order_amount > 1000:
    discount = 0.10  # 10% discount for battery-based toys
elif product_code == 2 and order_amount > 100:
    discount = 0.05  # 5% discount for key-based toys
elif product_code == 3 and order_amount > 500:
    discount = 0.10  # 10% discount for electrical charging-based toys
else:
    discount = 0  # No discount

# Calculate final amount after applying discount
final_amount = order_amount - (order_amount * discount)

# Output the final amount
print("Final amount to pay: Rs.", round(final_amount,2))
