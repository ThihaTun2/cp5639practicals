# Input, Processing, Output
#
# 1. Percentage Change
#
# PseudoCode
# get original_num
# get change
# result = original_num + (original_num * change)
# print original_num, change, result

original_num = float(input("Enter the original number to calculate : "))
change = float(input("Enter the change percentage you want to do to the original no (Eg 0.05 is 5% increase) : "))

result = original_num + (original_num * change)

print(f"Original: {original_num}, Change: {change}, Result: {result}")

# Decision Structures
#
# 2. Time of day
#
# PseudoCode
# get time_of_day
# get user_status
# if time_of_day less than 12
#     time_message = before
# else
#     time_message = after
# if user_status = coming
#     status_message = Hi!
# else
#     status_message = Bye!
# print time_message, user_status, status_message

time_of_day = int(input("Enter the current hour of the day (Between 0-23 hours) :"))
user_status = input("Are you coming or going? (Answer with 'coming' or 'going' only): ").lower()

if time_of_day < 12:
    time_message = "before"
else:
    time_message = "after"

if user_status == "coming":
    status_message = "Hi!"
else:
    status_message = "Bye!"

print(f"It is {time_message} noon and you are {user_status}. {status_message}")

# 3. Coffee orders
#
# PsuedoCode
# get coffee_type
# get size
# if size is small
#     price = 3
# else if size is medium
#     price = 4
# else
#     price = 5
#
# if coffee_type is white
#     price = price+1
#
# print price

coffee_type = input("Select your coffee type (white or  black): ").lower()
size = input("Select the size for your coffee (small, medium or large): ").lower()

if size == "small":
    price = 3
elif size == "medium":
    price = 4
else:
    price = 5

if coffee_type == "white":
    price += 1

print(f"The Price of your coffee is ${price}.")

# Repetition Structures
#
# 4. Coffee orders with error-checking
#
# PsuedoCode
# get coffee_tyoe
# while coffee_type is not white or black
#     get coffee_type
# get size
# while size is not small or medium or large
#     get size
# if size is small
#     price = 3
# else if size is medium
#     price = 4
# else
#     price = 5
#
# if coffee_type is white
#     price = price+1
#
# print price

coffee_type = input("Select your coffee type (white or  black): ").lower()
while coffee_type != "white" and coffee_type != "black":
    print("Invalid Selection. Please try again")
    coffee_type = input("Select your coffee type (white or  black): ").lower()

size = input("Select the size for your coffee (small, medium or large): ").lower()
while size != "small" and size != "medium" and size!= "large":
    print("Invalid Selection. Please try again")
    size = input("Select the size for your coffee (small, medium or large): ").lower()

if size == "small":
    price = 3
elif size == "medium":
    price = 4
else:
    price = 5

if coffee_type == "white":
    price += 1

print(f"The Price of your coffee is ${price}.")

# 5. Accumulation
#
# PseudoCode
# get low_input
# get high_input
# total = 0
# while low_input > high_input
#     get low_input
#     get high_input
# for i in range between low_input and high_input + 1
#     print i
#     total = total + i
# print total

low_input = int(input("Enter a low value: "))
high_input = int(input("Enter a high value: "))
total = 0

while low_input > high_input:
    print("Invalid Inputs. Please try again.")
    low_input = int(input("Enter a low value: "))
    high_input = int(input("Enter a high value: "))

for i in range(low_input, high_input+1):
    print(i, end=" ")
    total += i

print(f"totals: {total}")