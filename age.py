def calculate_age():
    # --- VALIDATE BIRTH YEAR ---
    while True:
        try:
            dobyear = int(input("Please enter the year you were born eg 2003: "))
            if 1900 <= dobyear <= 2026:
                break
            else:
                print("Invalid year! Please enter a year between 1900 and 2026.")
        except ValueError:
            print("Error: Please enter numbers only, no letters!")
            print("")

    # Calculates current age by subtracting birth year from current year
    current_year = 2026
    age = current_year - dobyear

    if age < 0:
        print("You haven't been born yet!")
    else:
        print(f"Your age is approximately {age} years old.")
    
    print()
    input("Press Enter to continue...")

if __name__ == "__main__":
    calculate_age()
