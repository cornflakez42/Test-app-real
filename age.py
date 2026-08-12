def calculate_age(user_text):
    try:
        dobyear = int(user_text)
        if not (1900 <= dobyear <= 2026):
            return "Invalid year! Enter between 1900 and 2026."
        
        current_year = 2026
        age = current_year - dobyear

        if age < 0:
            return "You haven't been born yet!"
        else:
            return f"Your age is approximately {age} years old."
    except ValueError:
        return "Error: Please enter numbers only!"
