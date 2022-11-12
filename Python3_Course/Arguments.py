# Your code below:

"""This is a module."""

def generate_trip_instructions(location):
    """This will source the location of the user and print a greeting."""
    print("Looks like you are planning a trip to visit " + (location))
    print("You can use the public subway system to get to " + (location))

generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")


# Write your code below:

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)


# Write your code below:

def trip_planner(first_destination=" Iceland", second_destination=" India", final_destination=" Germany"):
    print("Here is what your trip will look like!")
    print("First, we will stop in" + first_destination,
          ", then" + second_destination + ", and lastly" + final_destination)


trip_planner(" Brooklyn", " Queens")
