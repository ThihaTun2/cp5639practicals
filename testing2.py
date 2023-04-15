import datetime
import random

print("*******************************")
print("Universal Ride Ticketing System")
print("*******************************")

today = datetime.datetime.today()
ticket_price = 0
birthday_string = input("Enter birthday Eg: 1999/05/15 : ")
birthday = datetime.datetime.strptime(birthday_string, '%Y/%m/%d')
gift_selection = ["smartphone", "watch", "bicycle", "car", "movie ticket"]

pass_type = input("Enter WD or WK: ").lower()
while pass_type != "wd" and pass_type != "wk":
    print("Invalid input!")
    pass_type = input("Enter WD or WK: ").lower()

age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

if age < 5:
    if pass_type == "wd":
        ticket_price = 30
    else:
        ticket_price = 40
elif age <= 50:
    if pass_type == "wd":
        ticket_price = 50
    else:
        ticket_price = 60
else:
    if pass_type == "wd":
        ticket_price = 45
    else:
        ticket_price = 55

upgrade = input("Upgrade the ticket? Yes/NO ").lower()
while upgrade != "yes" and upgrade != "no":
    print("Invalid input!")
    upgrade = input("Upgrade the ticket? Yes/NO ").lower()

if today.month == birthday.month:
    birthday_gift = random.choice(gift_selection)
    print(f"Happy Birthday!! You won a {birthday_gift} as a birthday present.")

if upgrade == "yes":
    if pass_type == "wd":
        ticket_price += 20
    else:
        ticket_price += 30

print(f"Today is {today.strftime('%Y-%m-%d')}")
print(f"The cost of your ticket is {ticket_price}")