def calculate_age(user_input):
    try:
        birth_year = int(user_input)
        current_year = 2026
        age = current_year - birth_year
        if age < 0:
            return "You haven't been born yet!"
        return f"You are approximately {age} years old."
    except ValueError:
        return "Invalid year. Please enter numbers only."
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
            if 1900 <= dobyear <= today.year:
                break
            else:
                print(RED + f"Invalid year! Please enter a year between 1900 and {today.year}." + CYAN)
        except ValueError:
            print(RED + "Error: Please enter numbers only, no letters!" + CYAN)
            print("")

    #calculates current age by subtracting current year
    age = today.year - dobyear
    
    if dobm > today.month or (dobm == today.month and dobd > today.day):
        age -= 1

    print(f"{YELLOW}your name is {name.capitalize()} your age is {age} you were born {dobd}/{dobm}/{dobyear}")
    print()
    input(YELLOW + "Press Enter to return to menu..." + CYAN)
