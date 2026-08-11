MAGENTA = "\033[35m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# calculator func start
def calcu():
    calc = 0
    while True: 
        # --- VALIDATE FIRST NUMBER ---
        while True:
            try:
                numb1 = int(input(MAGENTA + "what is your first number: " + GREEN))
                break 
            except ValueError:
                print(RED + "Error: Please enter numbers only, no letters!" + GREEN)
                print()

        # --- SAFE OPERATOR INPUT FOR ANDROID ---
        while True:
            operator = input(MAGENTA + "please enter the operator (+, -, *, /): " + GREEN).strip()
            if operator in ["+", "-", "/", "*"]:
                break
            print(RED + "Invalid operator! Please enter +, -, *, or /." + GREEN)
            print()

        # --- VALIDATE SECOND NUMBER ---
        while True:
            try:
                numb2 = int(input(MAGENTA + "please enter the second number: " + GREEN))
                break 
            except ValueError:
                print(RED + "Error: Please enter numbers only, no letters!" + GREEN)
                print()
        
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
            
        print(operator) # Print the operator so the user sees what they pressed
        
        # --- INSTANT OPERATOR VALIDATION ---
        if operator not in ["+", "-", "/", "*"]:
            print(RED + "Invalid operator! Please enter +, -, *, or /." + GREEN)
            print()
            continue # Restarts the entire calculator function, bypassing numb2!
        # --- AUTO-ENTER OPERATOR LOGIC END ---

        # --- VALIDATE SECOND NUMBER ---
        while True:
            try:
                numb2 = int(input(MAGENTA + "please enter the second number: " + GREEN))
                break # Exits number 2 loop if it's a valid integer
            except ValueError:
                print(RED + "Error: Please enter numbers only, no letters!" + GREEN)
                print()
        
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

#calc end
