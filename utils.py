# utils.py


# Import libraries
import os
import platform
import sys


# Define wait function
def wait():
    input("\nPress Enter to continue... ")


# Define clear screen function
def clear():
    
    # Try to clear the terminal
    try:
        
        # Check which operating system is being used
        if platform.system() == "Windows":
            
            
            # For Windows, define ret as the 'cls' command to use later
            ret = os.system('cls')
            
        else:
            
            # For Mac/Linux, define ret as the 'clear' command to use later
            ret = os.system('clear')
    
        # If os.system returns non-zero, it means command failed
        if ret != 0:
            
            # Raise an exception if command failed
            raise Exception("Clear command failed")
        
    # If an exception is raised
    except Exception:

        # Fallback to printing many blank lines
        print("\n" * 50)
        
    # Flush output (forces output to appear immediately)
    sys.stdout.flush()
    
    # Return an empty string instead of None
    return ""