# main.py

# Import functions
from show_menu import show_menu
from add_idea import add_idea
from view_ideas import view_ideas
from delete_idea import delete_idea
from exit_vault import exit_vault
from utils import wait
from utils import clear

# Define function main
def main():
    
    # Print welcome message
    print ("\nWelcome to Idea Vault!\n")
    wait()
    
    # "while True:" loop to keep the program running after each choice and function
    while True:
        
        # Clear screen
        clear()
        
        # Show menu
        show_menu()
        
        # Get user choice from menu
        choice = input("Choose an option: ")
        
        # Call functions based on user choice
        if choice == "1":
            clear()
            add_idea()
            wait()
            clear()
        elif choice == "2":
            clear()
            view_ideas()
            wait()
            clear()
        elif choice == "3":
            clear()
            delete_idea()
            wait()
            clear()
        elif choice == "4":
            clear()
            exit_vault()
            break
        
        # If choice is invalid, print error message 
        else:
            print("\nInvalid choice.")
            wait()
            clear()

# Stops main function from immediately running if imported
if __name__ == "__main__":
    main()