"""
CP1401 2023 TR1 Assignment 1
Program 1 – Pizza Pay Calculator
Name: Thiha Tun
Date started: 18/04/2023
Pseudocode:

<pseudocode here>
"""

TRIP_RATE = 1.45
MINUTE_RATE = 0.95

print("Warm Pizza Pay Calculator")
trip_number = int(input("Number of trips: "))
minute_number = int(input("Number of minutes: "))

trip_pay = trip_number * TRIP_RATE
minute_pay = minute_number * MINUTE_RATE
total_pay = trip_pay + minute_pay

print(f"For {trip_number} trips, your pay is: ${trip_pay}")
print(f"For {minute_pay} minutes, your pay is: ${minute_pay}")
print(f"Your total pay is ${total_pay}")