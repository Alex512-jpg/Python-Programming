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


# area for the encryption process
unEncText = "myPassword" 
charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, " 
def encrypt(text):
    encText = ""
    for char in text:
        originalIndex = charSet.find(char)
        newIndex = (originalIndex + 3) % len(charSet)
        encChar = charSet[newIndex]
        encText += encChar
    return encText

# area for decrypting the information
def decrypt(text):
    encText = ""
    for char in text:
        originalIndex = charSet.find(char)
        newIndex = (originalIndex - 3) % len(charSet)
        encChar = charSet[newIndex]
        encText += encChar
    return encText

def savecredentials(website1, emailuser, pword):
    f = open("credentials.txt", "a")
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
        website1 = input(CLEAR + "\nWhat website will you be saving?\n\n").strip()
        emailuser = input(CLEAR + "\nEnter your Username/E-mail:\n\n").strip()
        pword = input(CLEAR + "\nEnter your Password:\n\n").strip()
        savecredentials(encrypt(website1), encrypt(emailuser), encrypt(pword))
        print(CLEAR + GREEN + "Credentials saved." + RESET)
        
    # process for the 'view credentials' feature
    elif choice == 'v':
        print(CLEAR)
        # Opening the file in read mode
        with open('credentials.txt', 'r') as file:
            content = file.readlines()
            for line in content:
               encWebsite, encEmail, encPass = line.strip().split('\t')
               print(decrypt(encWebsite), decrypt(encEmail), decrypt(encPass))
            input("\nPress Enter to return to Menu\n")
            print(CLEAR)
    elif choice == 'q':
        print("\nExiting Password Manager\n")
    else:
        print(CLEAR + YELLOW + "\nInvalid option, please try again.\n" + RESET)
        
# Print a message when exiting the program.
print(CLEAR + RED + "\n\n\n\nProgram exit." + RESET)