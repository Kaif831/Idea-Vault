# view_ideas.py

# Import data
from data import ideas

# Define function
def view_ideas():

    # Print title
    print("--- View saved ideas ---\n")
    
    # Check if ideas dictionary has any ideas
    if not ideas:
        
        #Print no ideas in ideas message
        print("No ideas saved yet.\n")
        
    # Print saved ideas
    else:
        print("\nSaved Ideas:\n")
        for id_num, idea in ideas.items():
            print(f"{id_num}. {idea}\n")