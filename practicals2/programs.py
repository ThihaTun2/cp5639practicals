# Example

original_price = float(input("Original price : $"))
surcharge_rate = float(input("Subcharge % (e.g. 0.15 is 15 percent"))
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
print("The total meal price is $", total_price, sep="")

# Question 1 Discount Price

original_price = float(input("Enter the original price of an item : "))
DISCOUNT_PERCENTAGE = 20
discounted_amount = original_price * (DISCOUNT_PERCENTAGE/100)
new_price = float(original_price - discounted_amount)
print(f"The new price of the item is {new_price}")

# Question 2 Kilometres to Miles

distance_in_kilometers = float(input("Enter the distance in kilometers : "))
CONVERSION_RATE = 0.621371
distance_in_miles = distance_in_kilometers * CONVERSION_RATE
print(f"The distance in miles is : {distance_in_miles}")

# Question 3 Holiday Cost

daily_hotel_cost = 75
daily_food_cost = float(input("Daily food cost : $"))
daily_activities_cost = float(input("Daily activities cost : $"))
holiday_days = int(input("Number of days : "))
total_costs = (daily_hotel_cost + daily_food_cost + daily_activities_cost) * holiday_days
print(f"The trip will cost ${total_costs}")

# Question 4 Deep Sleep Calculation (Percentage)

total_sleep_time_in_seconds = int(input("Total sleep in seconds :"))
deep_sleep_time_in_seconds = int(input("Deep sleep in seconds :"))
percentage_effectiveness = deep_sleep_time_in_seconds / total_sleep_time_in_seconds * 100

print(f"Deep Sleep : {deep_sleep_time_in_seconds // 60}m {deep_sleep_time_in_seconds % 60}s")
print(f"Total Sleep : {total_sleep_time_in_seconds //60}m {total_sleep_time_in_seconds %60}s")
print(f"Percentage : {percentage_effectiveness}%")
