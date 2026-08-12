def calculate():
    while True:
        user_input = input("Enter a math expression (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
            
        try:
            # Safely evaluate simple math expressions
            allowed_chars = set("0123456789+-*/.() ")
            if not all(char in allowed_chars for char in user_input):
                print("Invalid characters used in calculation.")
                continue
                
            result = eval(user_input)
            print(f"Result: {result}")
            print()
            input("Press Enter to continue...")
            break
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception:
            print("Invalid calculation expression.")

if __name__ == "__main__":
    calculate()
