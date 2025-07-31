# delete_idea.py

# Import data and functions
from data import ideas
    
# Import functions
from view_ideas import view_ideas
from utils import clear

# Define function
def delete_idea():

    # Print title
    print("--- Delete an idea ---\n")
    
    # Check if ideas dictionary has any ideas
    if not ideas:
        
        # Print no ideas message
        print("No ideas to delete.\n")
    
    # Start to ask which idea to delete and delete idea
    else:
        
        # Ask which idea to delete (user doesn't answer yet)
        print("Which idea number do you want to delete?\n")
        input ("Press Enter to view ideas... ")
        clear()
    
        # View ideas
        view_ideas()
        
        # Use while True loop to keep asking until valid input
        while True:
            
            # Try to convert user input to an integer
            try:
            
                # Ask which idea to delete (user answers here)
                delete_choice = int(input(f"{'\n' * 2}Enter idea number to delete: ").strip())
                
            # If input is not a number
            except ValueError:
                
                # Print error message
                print(f"{'\n' * 2}That's not a number. Please try again.")
                
                # Continue to ask for input
                continue
            
            # Check if delete choice is in ideas
            if delete_choice in ideas:
                
                # Delete idea
                deleted = ideas.pop(delete_choice)

                # Update idea numbers (rebuild "ideas" dict with new numbers)
                new_ideas = {i: idea for i, idea in enumerate(ideas.values(), start=1)}

                # Clear "ideas" dict to remove old numbers
                ideas.clear()

                # Update "ideas" dict with new version
                ideas.update(new_ideas)
                
                # Print success message
                print(f"""{'\n' * 2}Deleted idea #{delete_choice}: 

{deleted}""")
                
                # Break out of the loop
                break
            
            # If delete choice is not in ideas
            else:
                print(f"{'\n' * 2}Idea not found. Please try again.")