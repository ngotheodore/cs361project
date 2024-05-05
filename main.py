import os

main_options = [1,2,3,4,5,6]
help_options = [1,2,3,4,5]

def main_menu():
    while True:
        print("Program Options:")
        print("1. Add - Add an entry to the database")
        print("2. Browse - Browse entries in the database")
        print("3. Edit - Edit an entry in the database")
        print("4. Delete - Delete an entry in the database")
        print("5. Help - Provides instructions on how to use the different functions of the program")
        print("6. Quit - Exit the program")

        choice = int(input("\nPlease choose an option: "))

        if choice in main_options:
            return choice
        else:
            print("\nError: That option is not recognized")
            print("Please try again\n")

def add_screen():
    while True:
        title = input("Add the title: ")
        title = title + ''.join(".txt")
        file = open(title, "w")    
        content = input("Add the contents of the file: ")
        file.write(content)
        fav_choice = int(input("Enter 1 to add the file. Enter 2 to cancel and return to the menu: "))
        if fav_choice == 1:
            pass
        elif fav_choice == 2:
            file.close()
            os.remove(title)
            return
        else:
            print("\nError: That option is not recognized")
            print("Please try again\n")
        print("Would you like to mark the file as a favorite?")
        print("Enter 1 to mark as favorite. Enter 2 to not mark as favorite")
        print("Enter 1 to confirm the addition of the file. Enter 2 to cancel")

def browse_screen():
    print("Recent: ")
    print("Enter 1 to sort entries by a certain filter")
    print("You are currently on page #. Enter 2 to go to a certain page number")

def edit_screen():
    print("Text")

def delete_screen():
    title = input("Type in the file to delete (include the extension): ")

    os.remove(title)
def help_screen():
    while True:
        print("Help Screen Options:")
        print("1. How to add entries to the database")
        print("2. Browse screen features")
        print("3. Editing features")
        print("4. How to delete entries from the database")
        print("5. Return to main menu")

        choice = int(input("\nPlease choose an option: "))

        if choice in help_options:
            if choice == 1:
                add_help()
            elif choice == 2:
                browse_help()
            elif choice == 3:
                edit_help()
            elif choice == 4:
                delete_help()
            elif choice == 5:
                return
        else:
            print("\nError: That option is not recognized")
            print("Please try again\n")

def add_help():
    print("1. Add")

def browse_help():
    print("1. Add")

def edit_help():
    print("1. Add")

def delete_help():
    print("1. Add")

choice = 0

while choice != 6:
    choice = main_menu()
    if choice == 1:
        add_screen()
    elif choice == 2:
        browse_screen()
    elif choice == 3:
        edit_screen()
    elif choice == 4:
        delete_screen()
    elif choice == 5:
        help_screen()

print("\nTerminating Program")