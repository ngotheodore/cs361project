options = [1,2,3,4,5,6]

def main_menu():
    while True:
        print("Program Options:")
        print("1. Add - Add an entry to the database")
        print("2. Browse - Browse entries in the database")
        print("3. Edit - Edit an entry in the database")
        print("4. Delete - Delete an entry in the database")
        print("5. Help - Provides instructions on how to use the different functions of the program")
        print("6. Quit - Exit the program")

        choice = int(input("\nPlease choose an option>"))

        if choice in options:
            return choice
        else:
            print("\nError: That option is not recognized")
            print("Please try again\n")
        