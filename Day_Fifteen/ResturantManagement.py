# Restaurant menu stored in a dictionary
menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Pasta": 7.49,
    "Salad": 4.99,
    "Juice": 2.99
}

# Store customer's order with quantities
order = {}

# Function to display menu
def show_menu():
    print("\n--- Restaurant Menu ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

# Function to take an order
def take_order():
    while True:
        item = input("\nEnter the food item you want (or type 'done' to finish): ").title()
        
        if item == "Done":
            break  # Stop ordering
        
        if item in menu:
            qty = input(f"Enter quantity for {item}: ")
            if qty.isdigit():
                qty = int(qty)
                if item in order:
                    order[item] += qty
                else:
                    order[item] = qty
                print(f"{qty} {item}(s) added to your order!")
            else:
                print("Please enter a valid number.")
        else:
            print("Sorry, that item is not on the menu.")

# Function to generate and save the bill
def generate_bill():
    if not order:
        print("\nNo items ordered.")
        return
    
    total = 0
    bill_content = "\n--- Bill ---\n"
    
    for item, qty in order.items():
        price = menu[item] * qty
        bill_content += f"{item} (x{qty}): ${price:.2f}\n"
        total += price

    bill_content += f"\nTotal: ${total:.2f}\n"
    bill_content += "Thank you for dining with us!\n"

    # Display bill
    print(bill_content)

    # Save bill to a file
    with open("bill.txt", "w") as file:
        file.write(bill_content)
    print("Bill has been saved to 'bill.txt'.")

# Main program loop
while True:
    print("\n1. View Menu\n2. Order Food\n3. Get Bill & Save\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        take_order()
    elif choice == "3":
        generate_bill()
    elif choice == "4":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice, please try again.")
