# 🍽️ CLI Restaurant Billing System

## 📌 Overview
The **CLI Restaurant Billing System** is a simple Python script that allows users to:
- View a restaurant menu.
- Place an order with multiple items and quantities.
- Generate a bill and save it as a text file.

## 🚀 Features
- Displays a menu with prices.
- Allows customers to order multiple items.
- Calculates total bill and displays a receipt.
- Saves the bill to a text file (`bill.txt`).

## 🛠️ Built With
- Python 3.x
- `os` (built-in) for file handling

## 📥 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Burhanali2211/ResturantBillingSystem.git
   cd restaurant-billing-system
`
## Sample Output
```sh
1. View Menu
2. Order Food
3. Get Bill & Save
4. Exit
Enter your choice: 2

Enter the food item you want (or type 'done' to finish): Pizza
Enter quantity for Pizza: 2
2 Pizza(s) added to your order!

Enter the food item you want (or type 'done' to finish): Juice
Enter quantity for Juice: 1
1 Juice(s) added to your order!

Enter the food item you want (or type 'done' to finish): done

--- Bill ---
Pizza (x2): $17.98
Juice (x1): $2.99

Total: $20.97
Thank you for dining with us!

Bill has been saved to 'bill.txt'.
```
## 💡 Notes
Users can only order items available in the menu.
The script validates numeric input for quantity.
The generated bill is saved as a text file for future reference.

## 🛠️ Contributing
Feel free to contribute by improving the UI, adding more features, or enhancing functionality. Fork the repo and submit a pull request!

## 📜 License
This project is open-source and available under the MIT License.

## 👨‍💻 Developed By
Burhanali2211 - Creator of this CLI-based Restaurant Billing System.
