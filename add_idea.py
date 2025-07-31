# add_idea.py

# Import data
from data import ideas

# Define function
def add_idea():
    
    # Print title
    print("--- Add an idea ---\n")
    
    #Ask idea
    idea_text = input(f"Enter your idea:{'\n' * 2}").strip()
    
    # Create idea ID (number)
    new_id = len(ideas) + 1
    
    # Save idea
    ideas[new_id] = idea_text
    
    # Print success message
    print(f"{'\n' * 2}Idea #{new_id} saved!\n")