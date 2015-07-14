# Hotel occupancy rate calculator for each floor of a hotel
# Occupancy Rate = Number of rooms occupied/total number of rooms

# Write a program that calculates the occupancy rate for each floor
# of a hotel. The program should start by asking for the number of
# floors in the hotel. A loop should iterate once for each floor.
# During each iteration, the loop should ask the user for the number
# of rooms on the floor and the number of them that are occupied.
# After all iterations, the program should display the number of rooms
# the hotel has, the number of them that are occupied, the number that
# are vacant, and the occupancy rate for the hotel.

number_of_floors = 0  # Priming read
while number_of_floors < 1:
    number_of_floors = int(input("Please enter the number of floors in the hotel: "))

total_rooms = 0
rooms_occupied = 0
for each_floor in range(number_of_floors):
    rooms = int(input("Please enter the total number of rooms on the floor: "))
    if rooms < 1:
        rooms = int(input("Error: There must be 1 or more room(s). Please try again: "))
    else:
        total_rooms += rooms
    occupied = int(input("Please enter the total number of rooms occupied on this floor: "))
    if occupied < 0:
        occupied = int(input("Error: Rooms occupied cannot be less than 0. Please try again: "))
    else:
        rooms_occupied += occupied

rooms_vacant = total_rooms - rooms_occupied
occupancy_rate = rooms_occupied/total_rooms

print("The hotel has", number_of_floors, "floors with", total_rooms, "total rooms.")
print(rooms_occupied, "room(s) are occupied. The occupancy rate is", occupancy_rate)
