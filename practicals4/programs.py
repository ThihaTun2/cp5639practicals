# 1. Error Checking
#
# PseudoCode
#
# get worker_level
# while worker_level less than 1 or greater than 10
#     get worker_level again
# salary = worker_level * 5000
# print salary

BASE_SALARY = 5000
worker_level = int(input("Worker Level :"))

while worker_level < 1 or worker_level > 10:
    print("Invalid worker level")
    worker_level = int(input("Worker Level :"))

salary = worker_level * BASE_SALARY
print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")

# 2. Number Sequences
#
# a. Loop that shows all the odd numbers
#
# Pseudocode
#
# for number 1-100
#     if number divided by 2 remainder is 1
#         print number

REMAINDER = 1
for i in range(1, 101):
    remainder_value = i%2
    if remainder_value == REMAINDER:
        print(i)

# b. Loop that displays all Summer Olympic between 1896 and today
#    Summer Olympics are not held in 1916, 1940 and 1944 so those numbers are excluded.
#
# PseudoCode
#
# get thisyear
# for year between 1896 and thisyear
#     if year divided by 4 remainder is 0 and year is not 1916,1940 and 1944
#         print year end with spacing

START_YEAR = 1896
this_year = int(input("Enter this year: "))

for year in range(START_YEAR, this_year+1):
    remainder = year%4
    if remainder == 0 and year not in (1916, 1940, 1944):
        print(year, end=" ")

# c. Loop that represents meaningful sequence
#
# For this exercise I choose to use the Triangular Number Sequence. It shows the total number of dots arranged in all 3
# sides of a equilateral triangle. For example a triangle with a side that has 3 dots on each sides would have 6 dots
# total on all 3 sides.
#
# PsuedoCode
#
# get dots
# for i in 1 and dots+1
#     triangular_no = (i*(i+1)/2)

dots = int(input("Enter the number of dots you want in a side of a triangle: "))

for i in range(1, dots+1):
    trianglular_no = int((i*(i+1)/2))
    print(trianglular_no, end=" ")
# 3. Menu
#
# Pseudocode
# get user_input
# while user_input is not q
#     if user_input is s
#         show smiley face
#     else if user_input is f
#         show frowny face

print("(S)miley")
print("(F)rowny")
print("(Q)uit")
user_input = input("Press a key: ").lower()

while user_input != "q":
    if user_input == "s":
        print(":-)")
    elif user_input == "f":
        print(":-(")
    user_input = input("Press a key: ").lower()

print("Farewell")

# 4. Accumulation
#
# Average Age
#
# PseudoCode
#
# SENTINEL = -1
# total = 0
# no_of_people = 0
# get value
# while value != sentine
#     total = total + value
#     no_of_people = no_of_people + 1
#     get value
# average_age = total/no_of_people
# display average_age

SENTINEL = -1
total = 0
no_of_people = 0
value = int(input(f"Enter the age you want to calculate (Entering {SENTINEL} would quit the program: "))

while value != SENTINEL:
    total += value
    no_of_people += 1
    value = int(input(f"Enter the age you want to calculate (Entering {SENTINEL} would quit the program: "))

average_age = total/no_of_people
print(f"The average of the group is: {average_age}")

# Smileys Count
#
# Pseudocode

# smiley_count = 0
# frowny_count = 0
# get user_input
# while user_input is not q
#     if user_input is s
#         show smiley face
#         smiley_count = smiley_count + 1
#     else if user_input is f
#         show frowny face
#         frowny_count = frowny_count + 1
# display smiley_count and frowny_count

smiley_count = 0
frowny_count = 0
print("Smileys Count")
print("(S)miley")
print("(F)rowny")
print("(Q)uit")
user_input = input("Press a key: ").lower()

while user_input != "q":
    if user_input == "s":
        print(":-)")
        smiley_count += 1
    elif user_input == "f":
        print(":-(")
        frowny_count += 1
    user_input = input("Press a key: ").lower()

print(f"You have collected {smiley_count} smileys and {frowny_count} fronwnys.")

# Total Numbers
#
# PseudoCode
#
# total = 0
# get repetitions
# for i in range between repetition and 0
#     get value
#     total = total+value
# display total

total = 0
question_number = 1
repetitions = int(input("How many numbers do you want to add up? "))
for i in range(repetitions, 0, -1):
    value = int(input(f"Enter number {question_number}: "))
    total += value
    question_number += 1
print(f"The total of those {repetitions} numbers is {total}")

# 5. Guessing Game
#
# Pseudocode
#
# guess_no = 1
# get secret
# get guess_value
# while guess_value != secret
#     if guess_value < secret
#         print Higher
#     else
#         print Lower
#     guess_no = guess_no + 1
#     get guess_value
#
# print guess_no

guess_no = 1
secret = int(input("Enter the secret number: "))
guess_value = int(input("Guess a number: "))

while guess_value != secret:
    print("Guess again!")
    if guess_value < secret:
        print("Higher")
    else:
        print("Lower")

    guess_no +=1
    guess_value = int(input("Guess a number: "))

print(f"You got it in {guess_no} guesses!")

# 6. Nested Loops
#
# PseudoCodes
#
# get rows
# get columns
# for i in range rows
#     for i2 in range colums
#         print i2
#     skip line

rows = int(input("Rows : "))
columns = int(input("Columns : "))

for i in range (rows):
    for i2 in range (columns):
        print(i2, end=" ")
    print(" ")