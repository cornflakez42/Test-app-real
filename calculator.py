def calculate(user_text):
    try:
        # Safely evaluate simple math expressions
        allowed_chars = set("0123456789+-*/.() ")
        if not all(char in allowed_chars for char in user_text):
            return "Invalid characters used."
            
        result = eval(user_text)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception:
        return "Invalid calculation expression."
