def calculate(user_input):
    try:
        # Safely evaluate simple math expressions
        # (Restricted to basic safe characters for security)
        allowed_chars = set("0123456789+-*/.() ")
        if not all(char in allowed_chars for char in user_input):
            return "Invalid characters used in calculation."
            
        result = eval(user_input)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception:
        return "Invalid calculation expression."
        # --- MATH LOGIC ---
        if operator == "+":
            calc = numb1 + numb2
        elif operator == "-":
            calc = numb1 - numb2
        elif operator == "/":
            calc = numb1 / numb2
        elif operator == "*":
            calc = numb1 * numb2
            
        print(GREEN, numb1, operator, numb2, "=", calc)
        print()
        input(YELLOW + "Press Enter to return to menu..." + CYAN)
        break
        
