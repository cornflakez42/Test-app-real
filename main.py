# Import your other clean, mobile-safe Python scripts
from calculator import calcu
from guess_game_numb import game
from age import about

import os
import sys
import time

# Ensure Python can find local files in the package directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Colors
WHITE = "\033[1;37m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RED = "\033[31m"

# Main menu loop
while True:
    # Use standard screen clearing or print newlines if clear isn't supported on mobile
    os.system('clear')
    
    menu_prompt = YELLOW + "would you like to use " + MAGENTA + "calculator" + YELLOW + ", age, " + GREEN + "guessing " + RED + "exit?: " + CYAN
    choice = input(menu_prompt).lower().strip()
    
    if choice == "age":
        about()
    elif choice == "calculator" or choice == "calc":
        calcu()
    elif choice == "guess" or choice == "game":
        game()    
    elif choice == "exit" or choice == "q":
        print(GREEN + "bye")
        sys.exit(0)
    else:
        print(YELLOW + "Invalid option, please type calculator, age, guess, or exit.")
        time.sleep(1.5)
    elif choice =="guess" or choice =="game":
        game()    
    elif choice == "exit" or choice == "q":
        print(GREEN + "bye")
        sys.exit(0)
    else:
        print(YELLOW + "Invalid option, please type calculator, age, or exit.")
        time.sleep(1.5)
