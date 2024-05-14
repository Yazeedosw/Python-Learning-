#Birthday calculation project
import datetime


# Function to calculate age and day of birth
def calculate_age_and_day_of_birth(name, birthdate):
    try:
        birthdate = datetime.datetime.strptime(birthdate, '%d-%m-%Y')
        today = datetime.datetime.now()

        if birthdate > today:
            return f"Invalid date: {name}'s birthdate is in the future."

        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        day_of_birth = birthdate.strftime("%A")

        return f"{name} is {age} years old and she/he was born on {day_of_birth}"
    except ValueError:
        return f"Invalid date: {name}'s birthdate is not in the correct format or contains invalid values."


# Function to find oldest and youngest person
def find_oldest_and_youngest(people):
    if len(people) == 0:
        return "There are no people."
    elif len(people) == 1:
        return "There is no oldest or youngest person."

    ages = [person[1] for person in people]
    oldest_age = max(ages)
    youngest_age = min(ages)

    oldest_person = [person for person in people if person[1] == oldest_age][0]
    youngest_person = [person for person in people if person[1] == youngest_age][0]

    return f"The oldest one is {oldest_person[0]} and the youngest one is {youngest_person[0]}"


# Main function
def main():
    people = []
    while True:
        try:
            entry = input("Enter name and birthdate (dd-mm-yyyy), or press enter to finish: ").strip()
            if not entry:
                break

            name, birthdate = entry.split(', ')
            result = calculate_age_and_day_of_birth(name, birthdate)
            print(result)
            if "Invalid date" not in result:
                people.append((name, int(result.split()[2])))
        except Exception as e:
            print(e)

    print(find_oldest_and_youngest(people))
    print("Total People:", len(people))

    # Sorting people by age
    sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
    print("Sorted People (oldest to youngest):")
    for person in sorted_people:
        print(f"{person[0]} is {person[1]} years old")

    # Printing entries in reverse order
    print("Entries in reverse order:")
    for person in reversed(people):
        print(f"{person[0]}, {person[1]}")

    # Printing people born on Sunday
    print("People born on Sunday:")
    for person in people:
        birthdate = datetime.datetime.strptime(person[1], '%d-%m-%Y')
        if birthdate.strftime("%A") == "Sunday":
            print(person[0])


if __name__ == "__main__":
    main()
