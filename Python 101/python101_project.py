# Phone book creation project
phone_book = {'Amal': '1111111111',
              'Mohammed': '2222222222',
              'Khadijah': '3333333333',
              'Abdullah': '4444444444',
              'Rawan': '5555555555',
              'Faisal': '6666666666',
              'Layla': '7777777777'}

## Create a functions
def search_by_number(number):
    if number in phone_book.values():
        for Name, num in phone_book.items():
            if num == number:
                return Name
    else:
        return "Sorry, the number is not found "


def add_contact(name, number):
    phone_book[name] = number
    print("Contact added successfully!")

## Loop & if statement
while True:
    user_input_search = input('Enter a phone number or name,please/or write"End" to exit ')

    if user_input_search == "End":
        break

    if user_input_search.isdigit():
        if len(user_input_search) == 10:
            result = search_by_number(user_input_search)
            if result:
                print("Name:", result)
            else:
                print("Sorry, the number is not found")
        else:
            print("This is invalid number")
    else:
        if user_input_search in phone_book:
            print("Number:", phone_book(user_input_search))
        else:
            add_new = input("Name not found. Do you want to add it to the phone book? (yes/no): ")
            if add_new.lower() == 'yes':
                new_number = input("Enter the phone number: ")
                add_contact(user_input_search, new_number)
            else:
                print("Name not added.")
