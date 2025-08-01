# Idea Vault

## What is it?

Idea Vault is a simple text-based Python program that helps you store, view, and manage your ideas in one place. Perfect for capturing thoughts, project ideas, creative sparks, or anything else you want to remember.

## Features

- Add new ideas easily  
- View all saved ideas  
- Delete ideas you no longer need  
- Simple menu-driven interface in the terminal  
- No files needed - ideas are stored temporarily while the program runs
- A clear screen function is used to clear the terminal to stop it from getting messy

## How to Run

1. Make sure you have Python installed (version 3.x recommended).  
2. Download or clone all the files from this repository.  
3. Open your terminal or command prompt.  
4. Navigate to the folder containing the files.  
5. Run the program by typing:

    ```bash
    python idea_vault.py
    ```

6. Use the menu to add, view, or delete ideas.  
7. Ideas are stored temporarily (in memory) and will be lost once the program is closed.

## How it Works

- The program uses a list to keep track of all ideas during the session.  
- Ideas are lost when the program closes (no file saving yet).  
- The menu runs in a loop allowing continuous use until you exit.

## Example Flow

Here’s what a session might look like in the terminal (between each block the screen is cleared):

```plaintext
Welcome to Idea Vault!

What would you like to do?
1. Add a new idea
2. View all ideas
3. Delete an idea
4. Exit

Enter your choice (1-4): 1
```

```plaintext
Enter your idea: Build a solar-powered phone charger
Idea added successfully!
```

```plaintext
What would you like to do?
1. Add a new idea
2. View all ideas
3. Delete an idea
4. Exit

Enter your choice (1-4): 2
```

```plaintext
Saved Ideas:
1. Build a solar-powered phone charger
```

```plaintext
What would you like to do?
1. Add a new idea
2. View all ideas
3. Delete an idea
4. Exit

Enter your choice (1-4): 3
```
```plaintext
(Ideas are shown)

Which idea number do you want to delete? 1
Idea #1 deleted successfully!
```

```plaintext
What would you like to do?
1. Add a new idea
2. View all ideas
3. Delete an idea
4. Exit

Enter your choice (1-4): 4
```

```plaintext
We hope you enjoyed using Idea Vault and found it useful.
Goodbye!
```

## Future Improvements

- Save/load ideas to a file so they persist between sessions  
- Add categories or tags for ideas  
- Search and filter ideas  
- Prioritize or rate ideas  
- Export ideas to other formats
- Sort ideas in folders and/or sections