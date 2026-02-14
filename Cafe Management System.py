# Cafe Management System

# Menu dictionary
menu = {
    1: ("Coffee", 3),
    2: ("Tea", 2),
    3: ("Sandwich", 5),
    4: ("Cake", 4)
}

total_bill = 0
order_list = []

while True:
    print("\n------ Welcome to Python Cafe ------")
    print("1. Coffee - $3")
    print("2. Tea - $2")
    print("3. Sandwich - $5")
    print("4. Cake - $4")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice in menu:
        item_name, item_price = menu[choice]
        quantity = int(input(f"Enter quantity of {item_name}: "))
        
        total = item_price * quantity
        total_bill += total
        
        order_list.append((item_name, quantity, total))
        print(f"{item_name} added to cart. Subtotal: ${total}")

    elif choice == 5:
        print("\n------ Final Bill ------")
        
        for item in order_list:   # for loop
            print(f"{item[0]} x {item[1]} = ${item[2]}")
        
        print("Total Bill: $", total_bill)
        print("Thank you! Visit Again ☕")
        break   # exit while loop

    else:
        print("Invalid choice! Please try again.")
