MENU = ("1. List Phone Book\n2. Add Number\n3. Delete Number\n4. Update Number\n5. Quit\nEnter choice: ")
phonebook = {
    "Bill": "123456",
    "Jane": "234567",
    "Sven": "567890"
}

menu_selection = int(input(MENU))
while menu_selection != 5:
    if menu_selection == 1:
        for key, value in phonebook.items():
            print(key, ' -- ', value)

    elif menu_selection == 2:
        add_name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        while add_name == "" or phone_number == "":
            print("Fill up all of the revalent information. Data not added")
        else:
            phonebook[add_name] = phone_number

    elif menu_selection == 3:
        delete_name = input("Enter name: ")
        del phonebook[delete_name]
        print(f"{delete_name} is deleted")

    elif menu_selection == 4:
        update_name = input("Enter name: ")
        update_number = input("Enter new number: ")
        while update_name == "" or update_number == "":
            print("Fill up all of the revalent information.  Data not added")
        else:
            phonebook.update({update_name : update_number})
    else:
        print("Invalid Selection")

    menu_selection = int(input(f"\n{MENU}"))

print(f"You have {len(phonebook)} contacts in your phone book")