# Decision Structures
#
# 2. Time of day
#
# PseudoCode
# get time_of_day
# while time_of_day greater than 23 and less than 0
#     get time_of_day
# if time_of_day less than 12
#     time_message = before
# else
#     time_message = after
# get user_status
# while user_status is not coming or going
#     get user_status
# if user_status = coming
#     status_message = Hi!
# else
#     status_message = Bye!
# print time_message, user_status, status_message

time_of_day = int(input("Enter the current hour of the day (Between 0-23 hours) :"))
while time_of_day > 23 or time_of_day < 0:
    print("Your time is invalid please try again.")
    time_of_day = int(input("Enter the current hour of the day (Between 0-23 hours) :"))

if time_of_day < 12:
    time_message = "before"
else:
    time_message = "after"

user_status = input("Are you coming or going? (Answer with 'coming' or 'going' only): ").lower()
while user_status != "coming" and user_status != "going":
    print("Your input is invalid please try again.")
    print(user_status)
    user_status = input("Are you coming or going? (Answer with 'coming' or 'going' only): ").lower()

if user_status == "coming":
    status_message = "Hi!"
else:
    status_message = "Bye!"