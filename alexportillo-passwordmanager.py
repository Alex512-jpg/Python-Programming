# a set of colours used to visually distinct certain texts
GREEN = "\033[92m"
RESET = "\033[00m"
YELLOW = "\033[93m"
RED = "\033[91m"
# clears the screen for a cleaner menu and steps through it
CLEAR = "\033c"

# variables used for storing employee credentials
website1 = ''
emailuser = ''
pword = ''

f = open("totallynotpii.txt", "a")


def save_credentials(website1, emailuser, pword):
    f.write(website1 + "\t" + emailuser + "\t" + pword + "\n")

# Prints the title of the program for the company
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
    
    # process for the 'add credentials' feature
    if choice == 'a':
        website1 = input(CLEAR + "\nWhat website will you be saving?\n\n")
        emailuser = input(CLEAR + "\nEnter your Username/E-mail:\n\n")
        pword = input(CLEAR + "\nEnter your Password:\n\n")
        save_credentials(website1, emailuser, pword)
        print(CLEAR + GREEN + "Credentials saved." + RESET)
    # process for the 'view credentials' feature
    elif choice == 'v':
        
    elif choice == 'q':
        print("\nExiting Password Manager\n")
    else:
        print(YELLOW + "\nInvalid option, please try again.\n" + RESET)
        
# Print a message when exiting the program.
print(CLEAR + RED + "\n\n\n\nProgram exit." + RESET)

