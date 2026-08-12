from datetime import date

# Store state variables for the multi-step age flow
age_state = "get_name"
temp_name = ""
temp_day = 0
temp_month = 0

def reset_age_state():
    global age_state, temp_name, temp_day, temp_month
    age_state = "get_name"
    temp_name = ""
    temp_day = 0
    temp_month = 0

def process_age_input(user_text):
    global age_state, temp_name, temp_day, temp_month
    today = date.today()

    if age_state == "get_name":
        if not user_text.strip():
            return "Please enter a valid name.", "get_name"
        temp_name = user_text.strip().capitalize()
        age_state = "get_day"
        return f"Hello {temp_name}!\nPlease enter the day you were born (e.g. 07):", "get_day"

    elif age_state == "get_day":
        try:
            dobd = int(user_text)
            if 1 <= dobd <= 31:
                temp_day = dobd
                age_state = "get_month"
                return "Please enter the month you were born (e.g. 04):", "get_month"
            else:
                return "Invalid day! Please enter a number between 1 and 31.", "get_day"
        except ValueError:
            return "Error: Please enter numbers only for the day!", "get_day"

    elif age_state == "get_month":
        try:
            dobm = int(user_text)
            if 1 <= dobm <= 12:
                temp_month = dobm
                age_state = "get_year"
                return f"Please enter the year you were born (1900 - {today.year}):", "get_year"
            else:
                return "Invalid month! Please enter a number between 1 and 12.", "get_month"
        except ValueError:
            return "Error: Please enter numbers only for the month!", "get_month"

    elif age_state == "get_year":
        try:
            dobyear = int(user_text)
            if 1900 <= dobyear <= today.year:
                # Calculate final age
                age = today.year - dobyear
                if temp_month > today.month or (temp_month == today.month and temp_day > today.day):
                    age -= 1
                
                reset_age_state()
                return f"Your name is {temp_name}, age is {age}, born {temp_day:02d}/{temp_month:02d}/{dobyear}.\n(Press Submit to return to menu)", "done"
            else:
                return f"Invalid year! Enter between 1900 and {today.year}.", "get_year"
        except ValueError:
            return "Error: Please enter numbers only for the year!", "get_year"

    return "Choose an Option:\nage, calculator, guess", "menu"
