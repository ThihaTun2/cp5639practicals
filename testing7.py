"""
CP1401 2023 TR1 Assignment 1
Program 3 – Hiking Tracker
Name: Thiha Tun
Date started: 18/04/2023
Pseudocode:

<pseudocode here>
"""

DISTANCE_LIMIT = 120

total_distance = 0

print("Hiking Tracker")
day_number = int(input("Number of days: "))

while day_number <= 0:
    print("Invalid number of days")
    day_number = int(input("Number of days: "))

for i in range(1, day_number+1):
    distance_travelled = float(input(f"Day {i} distance: "))

    while distance_travelled < 0 or distance_travelled > DISTANCE_LIMIT:
        print("Invalid distance")
        distance_travelled = float(input(f"Day {i} distance: "))

    total_distance += distance_travelled

average_distance = total_distance / day_number

if distance_travelled == average_distance:
    final_text = "the same as your"
elif distance_travelled > average_distance:
    final_text = "above"
else:
    final_text = "below"

print(f"Your total distance was {total_distance}km")
print(f"Your average distance was {average_distance}km")
print(f"On your final day, your distance was {final_text} average.")
