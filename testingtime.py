GREEN = "\033[92m"
RESET = "\033[00m"
ORANGE = "\033[93m"
RED = "\033[91m"
CLEAR = "\033c"


# Give the user some context.
print(CLEAR)
print(GREEN + "\nThis program…………………………" + RESET)

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to create an encryption key.")
    print("[2] Enter 2 to …….")
    print("[3] Enter 3 to……")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice: ").lower().strip()
    
    # Respond to the user's choice.
    if choice == '1':
        print("\nEnter a name for the encryption key\n")
    elif choice == '2':
        print("\nEnter …….\n")
    elif choice == '3':
        print("\nEnter ……\n")
    elif choice == 'q':
        print("\nExiting the menu\n")
    else:
        print(ORANGE + "\nInvalid option, please try again.\n" + RESET)
        
# Print a message that we are all finished.
print(CLEAR + RED + "\n\n\n\nProgram exit." + RESET)