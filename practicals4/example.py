# Example

START_MONTH = 1
END_MONTH = 12
MIDDLE_MONTH = 6

birth_month = int(input(f"Enter month number ({START_MONTH}-{END_MONTH}): "))
while birth_month < START_MONTH or birth_month > END_MONTH:
    print("Invalid Month")
    birth_month = int(input(f"Enter month number ({START_MONTH}-{END_MONTH}): "))

for count in range (START_MONTH, birth_month+1):
    print(count, end=" ")
print()

if birth_month <=MIDDLE_MONTH:
    print("Your birth month is in the first half of the year.")
else:
    print("Your birth month is in the second half of the year.")

# 4. Accumulation Examples
#
# a. Sentinel
#
# PseudoCode from Question
#
# SENTINEL = -1
# total = 0
# get value
# while value != SENTINEL
#     total = total + value
#     get value
# display total

SENTINEL = -1
total = 0
value = int(input(f"Enter a number to add on.({SENTINEL} to quit the program): "))

while value!= SENTINEL:
    total = total + value
    value = int(input(f"Enter a number to add on.({SENTINEL} to quit the program): "))
print(f"The total of all the values are: {total}")

# b. Ask-the-user-to-quit
#
# PseudoCode from Question
# total = 0
# is_finished = False
# while not is_finished
#     get choice
#     if choice is quit
#          is_finished = True
#     else
#          get value
#          total = total + value
# display total

total = 0
is_finished = False

while is_finished == False:
    choice = input("Enter 'quit' to quit the program, any other inputs would continue the program : ").lower()
    if choice == "quit":
        is_finished = True
    else:
        value = int(input("Enter the number to add on: "))
        total = total + value

print(f"The total value is {total}")

# c. Definite Count
#
# PseudoCode from Question
#
# total = 0
# get count
# repeat count times
#     get value
#     total = total + value
# display total

total = 0
count = int(input("Enter the numbers of counts to add: "))
for i in range (count):
    value = int(input("Enter the number to add: "))
    total += value

print(f"The total value is {total}")