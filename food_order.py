def food_ordering_system():
    print("Welcome to Shruti's Food Court!")
    print("where every bite is a hug for your taste buds!!")
    menu = {
        'Starters': {
            1: ("Kebab Chaat", 120),
            2: ("Keema Samosa", 90),
            3: ("Delicious Butter Chicken", 180),
            4: ("Pani Puri", 60),
            5: ("Chicken Majestic", 150),
            6: ("Egg 65", 130),
            7: ("Samosas", 40),
            8: ("Pakoras", 70),
            9: ("Chaat", 50),
            10: ("Bhel Puri", 60),
            11: ("Dhokla", 40),
            12: ("Aloo Tikki", 60),
            13: ("Spring Rolls", 100)
        },
        'Main Course': {
            1: ("Paneer Butter Masala", 250),
            2: ("Veg Biryani", 180),
            3: ("Dal Tadka", 120),
            4: ("Chicken Biryani", 300),
            5: ("Butter Chicken", 350),
            6: ("Schezwan Chicken Rice", 280),
            7: ("Chicken Noodles", 220),
            8: ("Schezwan Veggies Noodles", 180),
            9: ("Matar Paneer", 200),
            10: ("Paneer Kofta Masala", 270),
            11: ("Veg Kolhapuri Tadka", 220),
            12: ("Kaju Masala", 240),
            13: ("Shev Kolhapuri Rassa", 230),
            14: ("Butter Naan", 40),
            15: ("Chapati", 30),
            16: ("Jeera Rice", 110)
        },
        'Desserts': {
            1: ("Pie", 150),
            2: ("Cobblers and Crumbles", 180),
            3: ("Cheesecake", 220),
            4: ("Banana Pudding", 100),
            5: ("Cakes and Cupcakes", 120),
            6: ("Brownies", 130),
            7: ("Ice Cream", 90),
            8: ("S'mores", 110),
            9: ("Fried Oreos", 160),
            10: ("Peach Cobbler Dump Cake", 170),
            11: ("Fresh Peach Turnovers", 140),
            12: ("Cookie Dough Brownies", 180),
            13: ("Loretta Lynn Dump Cake", 200)
        }
    }

    total_amount = 0
    ordered_items = []

    while True:
        print("\nChoose a category:")
        print("1. Starters")
        print("2. Main Course")
        print("3. Desserts")
        print("4. Exit")
        category_choice = int(input("Enter your choice (1-4): "))

        if category_choice == 4:
            break

        if category_choice == 1:
            category = 'Starters'
        elif category_choice == 2:
            category = 'Main Course'
        elif category_choice == 3:
            category = 'Desserts'
        else:
            print("Invalid category choice. Please try again.")
            continue

        print(f"\n{category} Menu:")
        for item_id, details in menu[category].items():
            print(f"{item_id}. {details[0]} - ₹{details[1]}")

        item_choice = int(input(f"Enter the item number to order from {category} (or 0 to go back): "))
        if item_choice == 0:
            continue

        if item_choice in menu[category]:
            quantity = int(input(f"How many {menu[category][item_choice][0]}s would you like to order? "))
            if quantity > 0:
                item_total = menu[category][item_choice][1] * quantity
                total_amount += item_total
                ordered_items.append((menu[category][item_choice][0], quantity, item_total))
                print(f"You ordered {quantity} {menu[category][item_choice][0]}(s) for ₹{item_total}.")
            else:
                print("Quantity must be greater than 0. Please try again.")
        else:
            print("Invalid item number. Please try again.")

        another_order = input("\nSir/Ma'am, would you like to have anything else? (yes/no): ").lower()
        if another_order != "yes":
            break

    # Final Bill
    print("\nThank you for your order! Here is your bill:")
    print("-------------------------------------------------")
    print("Item Name            Quantity     Total (₹)")
    print("-------------------------------------------------")
    for item_name, quantity, item_total in ordered_items:
        print(f"{item_name:<20} {quantity:<10} {item_total}")
    print("-------------------------------------------------")
    print(f"Grand Total: ₹{total_amount}")
    print("Visit again, Goodbye!")

food_ordering_system()
