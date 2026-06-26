 
'''
 
 4)Movie Ticket Booking Simulation
 -Simulate a movie theater booking system that:
 •Shows a list of available movie titles, showtimes, and seat prices.
 •Asks the user to choose a movie and number of tickets.
 •Confirms total price and asks if they want to book another movie.
 •Ends when they say "no" and displays total bookings and cost.

'''
print("Available Movies") 
movies = {
        1: {'title': 'Sankofa', 'time': '2:00 PM', 'price': 12.00},
        2: {'title': 'Harvest 3000 Years', 'time': '5:30 PM', 'price': 10.00},
        3: {'title': 'Teza', 'time': '8:00 PM', 'price': 8.00},
        4: {'title': 'Child of Resistance', 'time': '10:00 PM', 'price': 5.00}
    }
    
for number, movie in movies.items():
    print (f"{number}. {movie['title']}. show times {movie['time']} - Seat Price: ETB-{movie['price']:.2f}")

booking = []
total_cost = 0
total_tickets = 0
booking_count = 0

print("Welcome")
print("Movie Ticket Booking System ")

  
while True:
    booking = input("Enter item number (1-4) to choose a movie Choose):")
    booking = int(booking)
    if booking not in movies:
        print("Invalid selection. Please try again.")
        continue
    print(f"Movie: {movies[booking]['title']}")

    tickets = int(input("Enter number of tickets:"))
    print(f"Number of Tickets: {tickets}")
    Price = tickets * movies[booking]["price"]
    print("Total Price: ETB -", Price)
    print(f"show time: {movies[booking]['time']}")

 
    total_cost += Price
    total_tickets += tickets
    booking_count += 1
    Other_booking = input("Do you want to book another movie? (yes/no): ").lower()

    if Other_booking  == "no":
        break

print("Booking Summary ")
print(f"Total Bookings: {booking_count}")
print(f"Total Tickets: {total_tickets}")
print(f"Total Cost: ETB {total_cost}")
print("Thank you!")
    