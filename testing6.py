"""
CP1401 2023 TR1 Assignment 1
Program 2 – Device Time Determinator
Name: Thiha Tun
Date started: 18/04/2023
Pseudocode:

<pseudocode here>
"""

NOT_MOW_DEVICE_TIME = 0
MOW_DEVICE_TIME = 15
CUPCAKE_BONUS = 7

print("Device Time Determinator")
practice_number = int(input("Number of practices: "))
mow_status = input("Did you mow? ").lower()

if mow_status == "yes":
    device_time = practice_number * MOW_DEVICE_TIME
    print(f"You get {device_time} minutes of device time :)")
    if practice_number >= 7:
        print("And you get a cupcake!")

else:
    print("No device time :(")