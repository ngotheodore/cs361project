import os
import zmq
import requests
from datetime import date

context = zmq.Context()

socket_b = context.socket(zmq.REQ)
socket_b.connect("tcp://localhost:5556")
socket_c = context.socket(zmq.REQ)
socket_c.connect("tcp://localhost:5557")
socket_d = context.socket(zmq.REQ)
socket_d.connect("tcp://localhost:5558")
main_options = [1,2,3,4,5,6]
help_options = [1,2,3,4,5]
edit_options = [1,2,3,4]
browse_list = []
recent_list = []

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
            invalid_input()

def add_screen():
    title_confirm = "No"
    char_confirm = "No"
    content = ""
    while True:
        while title_confirm == "No":
            title = input("Add the title: ")
            socket_c.send(bytes(title, encoding='utf-8'))
            title_confirm = socket_c.recv()
            title_confirm = title_confirm.decode()
            if title_confirm == "No":
                print("Invalid character detected in title")
        title = title + ''.join(".txt")
        file = open(title, "w")
        text_choice = int(input("Would you like to add your own text or automatically generate text? Type 1 for yes, 2 for no: "))
        if text_choice == 1:
            content = auto_text()
            content = str(content)
        elif text_choice == 2:
            while char_confirm == "No":
                content = input("Add the contents of the file: ")
                socket_d.send(bytes(content, encoding='utf-8'))
                char_confirm = socket_d.recv()
                char_confirm = char_confirm.decode()
                if char_confirm == "No":
                    print("File exceeds character limit")
        file.write(content)
        first_confirm = int(input("Enter 1 to add the file. Enter anything else to cancel and return to the menu: "))
        if first_confirm == 1:
            pass
        else:
            file.close()
            os.remove(title)
            return
        print("Would you like to mark the file as a favorite?")
        fav_choice = int(input("Enter 1 to mark as favorite. Enter 2 to not mark as favorite: "))
        while True:
            if fav_choice == 1:
                favorite = True
                break
            elif fav_choice == 2:
                favorite = False
                break
            else:
                invalid_input()
                return
        second_confirm = int(input("Enter 1 to confirm the addition of the file. Enter anything else to cancel and return to the menu: "))
        if second_confirm == 1:
            print("Would you like to add a password to the file?")
            pass_choice = int(input("Enter 1 to add a password to the file. Enter 2 to create a file without a password: "))
            if pass_choice == 1:
                pass_type = int(input("Enter 1 to add your own password: "))
                if pass_type == 1:
                    password = custom_pass()
                    has_pass = True
                elif pass_type == 2:
                    password = auto_pass()
                    has_pass = True
                else:
                    invalid_input()
            elif pass_choice == 2:
                has_pass = False
                password = None
            else:
                invalid_input()
            file_date = date.today()
            new_entry = [title, favorite, file_date, has_pass, password]
            browse_list.append(new_entry)
            recent_list.append(new_entry)
            return
        else:
            file.close()
            os.remove(title)
            return

def browse_screen():
    while True:
        if (recent_list == False) or (browse_list == False):
            print("No entries detected. Returning to main menu")
            return
        else:
            print("Recent: ")
            for i in recent_list:
                for j in range(i):
                    print(recent_list[j][0], recent_list[j][2])
            print("Entries:")
            for i in browse_list:
                for j in range(i):
                    print(browse_list[j][0], browse_list[j][2])
            #print("Enter 1 to sort entries by a certain filter")
            #print("Enter 2 to search for an entry in the database")
            print("Enter 3 to quit")
            choice = int(input("\nPlease choose an option: "))
            if choice == 1:
                sort_func()
            elif choice == 2:
                search_func()
            elif choice == 3:
                return
            else:
                invalid_input()


def edit_screen():
    while True:
        current_file_name = input("Enter the title of the file: ")
        print("1. Edit the title of the file")
        print("2. Edit the contents of the file")
        print("3. Edit the favorite option on the file")
        print("4. Return to the main menu")

        choice = int(input("\nPlease choose an option: "))
        if choice == 1:
            new_file_name = input("Enter the new file name: ")
            os.rename(current_file_name, new_file_name)
            return
        elif choice == 2:
            content_choice = input("Enter 1 to add onto the contents of the file. Enter 2 to overwrite the contents of the file.")
            if content_choice == 1:
                file = open(current_file_name, "a")
                new_input = input("Enter the new text: ")
                file.write(new_input)
                file.close()
                return
            elif content_choice == 2:
                file = open(current_file_name, "w")
                new_input = input("Enter the new text: ")
                file.write(new_input)
                file.close()
                return
        elif choice == 3:
            print("Would you like to mark the file as a favorite?")
            fav_choice = int(input("Enter 1 to mark as favorite. Enter 2 to not mark as favorite: "))
            while True:
                if fav_choice == 1:
                    favorite = True
                    break
                elif fav_choice == 2:
                    favorite = False
                    break
                else:
                    invalid_input()
                    break
        elif choice == 4:
            return
        else:
            invalid_input()
    

def delete_screen():
    title = input("Type in the file to delete (include the extension): ")
    os.remove(title)
    recent_list.pop()
    browse_list.pop()

def help_screen():
    while True:
        print("Help Screen Options:")
        print("1. How to add entries to the database")
        print("2. Browse screen features")
        print("3. Editing features")
        print("4. How to delete entries from the database")
        print("5. File Constraints")
        print("6. Return to main menu")

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
                constraint_help()
            elif choice == 6:
                return
        else:
            invalid_input()

def add_help():
    print("1. Add a title for the file.")
    print("2. Add any text to the file")
    print("3. You will get a confirmation message. Enter an input to verify whether you want to add the file or not")
    print("4. You will be prompted to add the file as a favorite. Enter an input to verify if you want to add the file as a favorite or not")
    print("5. A second confirmation message will pop up. Enter an input to verify whether you want to add the file or not.")
    print("6. The file will be added to the array.")

def browse_help():
    print("1. The browse screen will show all the entries created thus far.")
    print("2. Inputting 1 will allow you to sort the entries by certain filters.")

def edit_help():
    print("1. Add")

def delete_help():
    print("1. Type in the name of the file. The extension must be included")
    print("2. The file will be removed from the database.")

def constraint_help():
    print("1. File titles cannot have the following characters: !@#$%^&*")
    print("2. Files have a character limit of 100 characters")
    print("3. File passwords must be at least be 10 characters long")

def invalid_input():
    print("\nError: That option is not recognized")
    print("Please try again\n")
    return

def auto_text():
    response = requests.get('http://localhost:5001/facts')
    data = response.json()
    return data

def sort_func():
    pass

def search_func():
    pass

def custom_pass():
    confirm = "No"
    while True:
        while confirm == "No":
            password = input("Enter a password. The password must be at least 10 characters long: ")
            socket_b.send(bytes(password, encoding='utf-8'))
            confirm = socket_b.recv()
            confirm = confirm.decode()
            if confirm == "No":
                print("Password does not meet length requirement")
        choice = int(input("Do you want to confirm this password? Type 1 to confirm, type 2 to try again: "))
        if choice == 1:
            return password
        elif choice == 2:
            pass
        else:
            invalid_input()

def auto_pass():
    pass
            
if __name__ == '__main__':

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
        else:
            invalid_input()

    print("\nTerminating Program")
