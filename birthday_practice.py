def look_up(birthdays):
    name = input("Enter your friend's name: ").strip()
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}.")
    else:
        print("That name was not found.")


def add_birthday(birthdays):
    name = input("Enter your friend's name: ").strip()
    if not name:
        print("The name cannot be empty.")
    elif name in birthdays:
        print("That name already exists. Choose option 3 to change it.")
    else:
        birthday = input("Enter the birthday (MM/DD/YYYY): ").strip()
        if birthday:
            birthdays[name] = birthday
            print("Birthday added.")
        else:
            print("The birthday cannot be empty.")


def change_birthday(birthdays):
    name = input("Enter your friend's name: ").strip()
    if name in birthdays:
        birthday = input("Enter the new birthday (MM/DD/YYYY): ").strip()
        if birthday:
            birthdays[name] = birthday
            print("Birthday updated.")
        else:
            print("The birthday cannot be empty.")
    else:
        print("That name was not found.")


def delete_birthday(birthdays):
    name = input("Enter your friend's name: ").strip()
    if name in birthdays:
        del birthdays[name]
        print("Birthday deleted.")
    else:
        print("That name was not found.")


def quit_program():
    print("Goodbye!")


def main():
    birthdays = {}

    while True:
        print("\nBirthday Menu")
        print("1. Look up a birthday")
        print("2. Add a new birthday")
        print("3. Change a birthday")
        print("4. Delete a birthday")
        print("5. Quit the program")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            look_up(birthdays)
        elif choice == "2":
            add_birthday(birthdays)
        elif choice == "3":
            change_birthday(birthdays)
        elif choice == "4":
            delete_birthday(birthdays)
        elif choice == "5":
            quit_program()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
