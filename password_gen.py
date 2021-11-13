##program to generate unique password based on user input specifications##
##########################################################################

import random
import string

password = ''
characters = string.ascii_lowercase


##user input for length
print("How many characters should your password be?")
length = int(input())

##user input for special characters
while(True):
    print("Would you like to include special characters like '?&$@#'? (y/n)")
    specChar = input()
    if specChar == 'y':
        print("You bet!")
        characters = characters + string.punctuation
        break
    elif specChar == 'n':
        print("I'll make sure to avoid special characters.")
        break
    else:
        print("Please enter 'y' or 'n'")

##user input for spaces
while (True):
    print("Would you like to include spaces? (y/n)")
    spaceChar = input()
    spaces = ' '
    if spaceChar == 'y':
        print("You bet!")
        characters = characters + spaces
        break
    elif spaceChar == 'n':
        print("I'll make sure to avoid spaces.")
        break
    else:
        print("Please enter 'y' or 'n'")
  
##user input for capitalilzation
while (True):
    print("Would you like to include capital letters? (y/n)")
    spaceChar = input()
    if spaceChar == 'y':
        print("You bet!")
        characters = characters + string.ascii_uppercase
        break
    elif spaceChar == 'n':
        print("I'll make sure to avoid capitalization.")
        break
    else:
        print("Please enter 'y' or 'n'")
        
##user input for numbers
while (True):
    print("Would you like to include numbers? (y/n)")
    numChar = input()
    if numChar == 'y':
        print("You bet!")
        characters = characters + string.digits
        break
    elif numChar == 'n':
        print("I'll make sure to avoid adding numbers.")
        break
    else:
        print("Please enter 'y' or 'n'")


password = ''.join(random.choice(characters) for i in range(length))

print("Your new password is: \n" + password + "\nDon't let anybody else see it!")