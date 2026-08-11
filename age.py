#imports
from datetime import date
import os

YELLOW = "\033[33m"
CYAN = "\033[36m"
RED = "\033[31m"

# function  age calc
def about():
    #gets todays date
    today = date.today()
    
    #asks then store name from the input str
    name = input(YELLOW+"what is ur name? "+CYAN).capitalize()
    os.system('clear')
    print("")
    
    #adding validation
    while True:
        try:
            dobd = int(input(YELLOW+"please enter the day u were born eg 07 "+CYAN))
            if 1 <= dobd <= 31: # Optional check to make sure day is a real calendar number
                break
            else:
                print(RED + "Invalid day! Please enter a number between 1 and 31." + CYAN)
        except ValueError:
            print(RED + "Error: Please enter numbers only, no letters!" + CYAN)
            print("")
             
    #same as line 11
    while True:
        try:
            dobm = int(input(YELLOW+"please enter the month u were born eg 04 "+CYAN))
            if 1 <= dobm <= 12: # Optional check to make sure month is a real calendar number
                break
            else:
                print(RED + "Invalid month! Please enter a number between 1 and 12." + CYAN)
        except ValueError:
            print(RED + "Error: Please enter numbers only, no letters!" + CYAN)
            print("")
            
    os.system('clear')
    print("")
      
    # --- VALIDATE BIRTH YEAR ---
    while True:
        try:
            dobyear = int(input(YELLOW+"Please enter the year you were born eg 2003 "+CYAN))
            if 1900 <= dobyear <= today.year: # Makes sure they don't type a future year
                break
            else:
                print(RED + f"Invalid year! Please enter a year between 1900 and {today.year}." + CYAN)
        except ValueError:
            print(RED + "Error: Please enter numbers only, no letters!" + CYAN)
            print("")

    #calculates current age by subtracting current year
    age = today.year - dobyear
    
    # corrected calculation bounds check logic for birthdays
    if dobm > today.month or (dobm == today.month and dobd > today.day):
        age -= 1

    #puts it all together and print the tezt back with the stored variables
    print(f"{YELLOW}your name is {name.capitalize()} your age is {age} you were born {dobd}/{dobm}/{dobyear}")
    print()
    input(YELLOW + "Press Enter to return to menu..." + CYAN)
