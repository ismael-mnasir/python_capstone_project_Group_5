# python_capstone_project_Group_5
Python Project 
# Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Ask the user to choose items by number in a loop.
#  Keeps track of selected items and their prices.
# Ends when the user types "done".
# Finally prints a receipt showing: List of selected items with prices and total cost

# Displays a list of snacks and drinks with item numbers and prices.
# Menu of snacks and drinks with item numbers and prices
menu_snacks_drinks = {
    1: {"name": "Snickers", "price": 2.50},
    2: {"name": "Coca Cola", "price": 3.00},
    3: {"name": "Pepsi", "price": 3.25},
    4: {"name": "Kit Kat", "price": 2.25},
    5: {"name": "Water", "price": 1.00},
    6: {"name": "Chips", "price": 3.50}
}

print("Menu List:")
for number, info in menu_snacks_drinks.items():
    print(f"{number}. {info['name']} - ${info['price']:.2f}")

# Ask the user to choose items by number in a loop.

Choices = []
total_cost = 0

while True:
    choice = input("Enter item number (or 0 to stop): ")
    choice = int(choice)

    if choice == 0:
        print("You stopped selecting items.")
        break

    if choice in menu_snacks_drinks:
        item = menu_snacks_drinks[choice]
        Choices.append(item)
        total_cost += item['price']
        print(f"You selected: {item['name']} - ${item['price']:.2f}")
    else:
        print("Invalid item number. Try again.")

print("\nReceipt:")
for item in Choices:
    print(f"{item['name']} - ${item['price']:.2f}")

print(f"Total cost: ${total_cost:.2f}")  

# Receipt: Snickers - $2.50, Pepsi - $3.25, Chips - $3.50; Total cost: $9.25


2. # Write a program that:
# Has a predefined dictionary of groceries with prices.

# Lets the user "add" items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.

# Grocery items and their pricesckout

grocery = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2,
    "egg": 5,
    "tomato": 2.5
}

# This will store what the user adds 
cart = {}

# Keep asking the user for items

while True:
    item = input("Enter item name (or type 'checkout' to finish): ").lower()

    # Stop when user types checkout
    if item == "checkout":
        break

    # Check if the item exists in our list
    if item in grocery:
        qty = int(input("Enter quantity: "))

        # If item already added before, just increase quantity
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
    else:
        print("Item not available")

# Show final bill
print("\nFinal Bill")
print("---------------------")
total = 0

# This loop goes through all items in the cart
for item in cart:
    price = grocery[item]
    qty = cart[item]
    subtotal = price * qty

    # Show each item with quantity and subtotal
    print(f"{item} | Qty: {qty} | Subtotal: {subtotal}")

    total += subtotal

# Show total price
print("Total:", total)

This program lets a user add grocery items, stores them in a cart, and calculates the total bill at the end


Build a to-do list manager that

Allows users to add tasks with priorities (e.g., "Buy milk - high").
Lets them view the current list, delete tasks by number, and mark tasks as complete.
Keeps looping until the user types "exit".
Shows a summary at the end: number of completed tasks vs pending.

tasks = []   # List to store all tasks as dictionaries

while True:   # Main loop that keeps the program running
    print("\n===== GROUP 5 TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("Type 'exit' to quit")

    choice = input("\nChoose an option: ").strip().lower()  # Clean user input

    # --- EXIT PROGRAM ---
    if choice == "exit":
        break   # Stop the loop and move to summary

    # --- ADD TASK ---
    elif choice == "1":
        task_name = input("Enter task: ")
        priority = input("Enter priority (high/medium/low): ")

        # Create a task dictionary
        task = {
            "name": task_name,
            "priority": priority,
            "completed": False   # New tasks start as not completed
        }

        tasks.append(task)   # Add task to the list
        print("Task added successfully!")

    # --- VIEW TASKS ---
    elif choice == "2":
        if not tasks:   # Check if list is empty
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):   # Number each task
                status = "✓ Completed" if task["completed"] else "✗ Pending"
                print(f"{i}. {task['name']} (Priority: {task['priority']}) - {status}")

    # --- MARK TASK AS COMPLETE ---
    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            # Show tasks with their status
            for i, task in enumerate(tasks, start=1):
                status = "✓ Completed" if task["completed"] else "✗ Pending"
                print(f"{i}. {task['name']} - {status}")

            try:
                task_num = int(input("Enter task number to mark complete: "))
                # Validate number
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True   # Mark as complete
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # --- DELETE TASK ---
    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            # Show tasks with numbers
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            try:
                task_num = int(input("Enter task number to delete: "))
                # Validate number
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)   # Remove task
                    print(f"Deleted: {removed['name']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # --- INVALID OPTION ---
    else:
        print("Invalid option. Try again.")

# --- SUMMARY AFTER EXIT ---
completed = sum(task["completed"] for task in tasks)   # Count completed tasks
pending = len(tasks) - completed                       # Count pending tasks

print("\n===== SUMMARY =====")
print(f"Completed Tasks: {completed}")
print(f"Pending Tasks: {pending}")
print("Goodbye!")

#  Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say "no" and displays total bookings and cost
# Ditionary of available movies with details
movies = {
    1: {'title': 'Sankofa', 'time': '2:00 PM', 'price': 12.00},
    2: {'title': 'Harvest 3000 Years', 'time': '5:30 PM', 'price': 10.00},
    3: {'title': 'Teza', 'time': '8:00 PM', 'price': 8.00},
    4: {'title': 'Child of Resistance', 'time': '10:00 PM', 'price': 5.00}
}

# Display available movies
print("Available Movies")
for number, movie in movies.items():
    print(f"{number}. {movie['title']} - Show Time: {movie['time']} - Seat Price: ETB {movie['price']:.2f}")

# Variables to track totals
total_cost = 0
total_tickets = 0
booking_count = 0

print("\nWelcome to the Movie Ticket Booking System!")

# Main booking loop
while True:
    # Ask user to choose a movie
    booking = input("Enter movie number (1-4): ")

    # Convert input to integer
    try:
        booking = int(booking)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Validate movie selection
    if booking not in movies:
        print("Invalid selection. Please try again.")
        continue

    # Show selected movie
    print(f"\nMovie Selected: {movies[booking]['title']}")

    # Ask for number of tickets
    try:
        tickets = int(input("Enter number of tickets: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    print(f"Number of Tickets: {tickets}")

    # Calculate price
    price = tickets * movies[booking]["price"]
    print(f"Total Price: ETB {price}")
    print(f"Show Time: {movies[booking]['time']}")

    # Update totals
    total_cost += price
    total_tickets += tickets
    booking_count += 1

    # Ask if user wants another booking
    other_booking = input("Do you want to book another movie? (yes/no): ").lower()

    if other_booking == "no":
        break

# Final summary
print("\n===== BOOKING SUMMARY =====")
print(f"Total Bookings: {booking_count}")
print(f"Total Tickets: {total_tickets}")
print(f"Total Cost: ETB {total_cost}")
print("Thank you for booking with us!")
