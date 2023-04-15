# 1. Tax

# PseudoCode
# get income
# if income < 100
#     take_home_pay = income
# elseif income >= 100 and income <= 1000
#     take_home_pay = income - (income * 0.05)
# else
#     take_home_pay = income - (income * 0.1)
#
TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_NEW = 0.02
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_NEW = 500
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
# TODO: complete this part of the program here
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif income < TAX_THRESHOLD_NEW:
    total_tax = income * TAX_RATE_NEW
elif income < TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
else:
    total_tax = income * TAX_RATE_HIGH

take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# 2. Car Insurance
#
# Pseudocode
# get applicant_age
# if applicant_age less than 18
#     refuse hire
# else if applicant_age less than 25
#     ask to purchase special insurance
# else
#     tell insurance not required

REFUSED_THRESHOLD = 18
SPECIAL_INSURANCE_THRESHOLD = 25

applicant_age = int(input("Enter your age (in years): "))

if applicant_age < REFUSED_THRESHOLD:
    print("Hire refused")
elif applicant_age < SPECIAL_INSURANCE_THRESHOLD:
    print("Insurance required")
else:
    print("Insurance not required")

# 3. Simple Password Checker
#
# Pseudocode
# get input_password
# if input_password equals stored_password
#     grant access
# else
#     deny access

PASSWORD = "testpassword"

input_password = input("Enter your password here : ")

if input_password == PASSWORD:
    print("Access granted")
else:
    print("Access denied")

# 4. Dog Years
#
# Pseudocode
# get human_year
# if human_year <= 2
#     dog_year = human_year * 10.5
# else
#     dog_year = (human_year * 10.5) + ((human_year - 2) * 4)
# print dog_year

HUMAN_YEAR_THRESHOLD = 2
FIRST_TWO_YEARS_THRESHOLD = 10.5
LATER_YEARS_THRESHOLD = 4

human_year = int(input("Age in human years : "))

if human_year <= HUMAN_YEAR_THRESHOLD:
    dog_year = human_year * FIRST_TWO_YEARS_THRESHOLD
else:
    dog_year = (HUMAN_YEAR_THRESHOLD * FIRST_TWO_YEARS_THRESHOLD) + ((human_year - HUMAN_YEAR_THRESHOLD) * LATER_YEARS_THRESHOLD)

print(f"Age in dog years is {dog_year}")

# 5. Rock of Ages
#
# Pseudocode
# get user_age
# if user_age < 0 or user_age > 120
#     Invalid Age
# else if user_age <= 20
#     print Trivia1
# else if user_age <=40
#     print Triva2
# else if user_age <=60
#     print Trivia3
# else if user_age<=80
#     print Trivia4
# else if user_age<=100
#     print Trivia5
# else
#     print Trivia5

AGE_LOWER_LIMIT = 0
AGE_UPPER_LIMIT = 120

AGE_THRESHOLD_1 = 20
AGE_THRESHOLD_2 = 40
AGE_THRESHOLD_3 = 60
AGE_THRESHOLD_4 = 80
AGE_THRESHOLD_5 = 100

user_age = int(input("Enter your age : "))

if user_age < AGE_LOWER_LIMIT or user_age > AGE_UPPER_LIMIT:
    print("Invalid age")
elif user_age <= AGE_THRESHOLD_1:
    print("All of you are born in the 21st century.")
elif user_age <= AGE_THRESHOLD_2:
    print("All of you are young adults or still young enough to pretend to be one.")
elif user_age <= AGE_THRESHOLD_3:
    print("All of you are in their middle ages.")
elif user_age <= AGE_THRESHOLD_4:
    print("You are starting to feels old")
elif user_age <= AGE_THRESHOLD_5:
    print("You are close to enough to be 100 years old or is 100 years old")
else:
    print("Congrats you have lived through a entire century")

# 6. Speeding Fines
#
# Pseudocode
# get user_going_speed
# get speed_limit
# speed_over_limit = user_going_speed - speed_limit
# if speed_over_limit <=0
#     User not going over speed limit
# else if speed_over_limit < 13
#     Fine amount is $177
# else if speed_over_limit <= 20
#     Fine amount is $266
# else if speed_over_limit <=30
#     Fine amount is $444
# else if speed_over_limit <=40
#     Fine amount is $622
# else
#     Fine amount is $1245

DEMERIT_1 = int(13)
DEMERIT_1_FINE = int(177)

DEMERIT_3 = int(20)
DEMERIT_3_FINE = int(266)

DEMERIT_4 = int(30)
DEMERIT_4_FINE = int(444)

DEMERIT_6 = int(40)
DEMERIT_6_FINE = int(622)

DEMERIT_8_FINE = int(1245)

user_going_speed = int(input("Enter your speed in km/h : "))
speed_limit = int(input("Enter the speed limit of the area in km/h : "))
speed_over_limit = user_going_speed - speed_limit

if speed_over_limit <= 0:
    print("You are not going over the speed limit.")
elif speed_over_limit < DEMERIT_1:
    print(f"Fine Amount : ${DEMERIT_1_FINE}")
elif speed_over_limit <= DEMERIT_3:
    print(f"Fine Amount : ${DEMERIT_3_FINE}")
elif speed_over_limit <= DEMERIT_4:
    print(f"Fine Amount : ${DEMERIT_4_FINE}")
elif speed_over_limit <= DEMERIT_6:
    print(f"Fine Amount : ${DEMERIT_6_FINE}")
else:
    print(f"Fine Amount : ${DEMERIT_8_FINE}")
