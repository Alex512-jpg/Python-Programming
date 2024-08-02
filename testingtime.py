GREEN = "\033[92m"
RESET = "\033[00m"
ORANGE = "\033[93m"
RED = "\033[91m"
CLEAR = "\033c"

website1 = ''
email1 = ''
passw = ''

# Give the user some context.
print(CLEAR)
print(GREEN + "\nDIGICORE PASSWORD MANAGER" + RESET)

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[A] Add Credentials")
    print("[V] View Credentials")
    print("[Q] Quit Password Manager")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice: ").lower().strip()
    
    # Respond to the user's choice.
    if choice == 'a':
        print(CLEAR + "\nWhat website credentials will you be storing?")
    elif choice == 'v':
        print("\nEnter …….\n")
    elif choice == 'q':
        print("\nExiting Password Manager\n")
    else:
        print(ORANGE + "\nInvalid option, please try again.\n" + RESET)
        
# Print a message that we are all finished.
print(CLEAR + RED + "\n\n\n\nProgram exit." + RESET)