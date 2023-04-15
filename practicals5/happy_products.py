# PseudoCode
# get user_choice
# while user_choice is not q
#     if user_choice is i
#         print instructions
#         get user_choice
#     else if user choice is c
#         get product_number
#         while product_number is less than 0
#             get product_number
#         get product_price
#         while product_price is less than 0
#             get product_price
#         total_price = product_number * product_price
#         if product_number > 5
#             total_price = total_price * 0.9
#         print product_number, product_price, total_price
#         get user_choice
#     else
#         print error message
#         get user_choice
# print farewell message

START = "Menu: \n(I)nstructions \n(C)alculate \n(Q)uit"

print(START)
user_choice = input("Choice: ").lower()

while user_choice != "q":
    if user_choice == "i":
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
        print(START)
        user_choice = input("Choice: ").lower()

    elif user_choice == "c":
        product_number = int(input("Number of products: "))
        while product_number < 0:
            print("Invalid input")
            product_number = int(input("Number of products: "))
        product_price = float(input("Price: "))
        while product_price < 0:
            print("Invalid input")
            product_price = float(input("Price: "))
        total_price = product_number * product_price

        if product_number > 5:
            total_price = total_price * 0.9

        print(f"{product_number} x ${product_price} = ${round(total_price,2)}")
        print(START)
        user_choice = input("Choice: ").lower()

    else:
        print("Invalid Choice")
        print(START)
        user_choice = input("Choice: ").lower()

print("Farewell")