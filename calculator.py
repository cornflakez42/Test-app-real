calc_state = "get_numb1"
numb1 = 0
operator = ""

def reset_calc_state():
    global calc_state, numb1, operator
    calc_state = "get_numb1"
    numb1 = 0
    operator = ""

def process_calculator_input(user_text):
    global calc_state, numb1, operator

    if calc_state == "get_numb1":
        try:
            numb1 = int(user_text)
            calc_state = "get_operator"
            return "Enter the operator (+, -, *, /):", "get_operator"
        except ValueError:
            return "Error: Please enter numbers only for the first number!", "get_numb1"

    elif calc_state == "get_operator":
        op = user_text.strip()
        if op in ["+", "-", "/", "*"]:
            operator = op
            calc_state = "get_numb2"
            return f"Expression: {numb1} {operator} [?]\nEnter the second number:", "get_numb2"
        else:
            return "Invalid operator! Please enter +, -, *, or /.", "get_operator"

    elif calc_state == "get_numb2":
        try:
            numb2 = int(user_text)
            if operator == "/":
                if numb2 == 0:
                    reset_calc_state()
                    return "Error: Cannot divide by zero!\n(Press Submit to return to menu)", "done"
                calc = numb1 / numb2
            elif operator == "+":
                calc = numb1 + numb2
            elif operator == "-":
                calc = numb1 - numb2
            elif operator == "*":
                calc = numb1 * numb2

            reset_calc_state()
            return f"Result: {numb1} {operator} {numb2} = {calc}\n(Press Submit to return to menu)", "done"
        except ValueError:
            return "Error: Please enter numbers only for the second number!", "get_numb2"

    return "Calculator Menu", "menu"
