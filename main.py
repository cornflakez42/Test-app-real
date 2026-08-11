
#import other py files
from calculator import calcu
from guess_game_numb import game
from age import about


#pylint:disable=C0303
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import time




#colors#
WHITE = "\033[1;37m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RED = "\033[31m"


# Main menu

while True:
    os.system('clear')
    menu_prompt = YELLOW + "would you like to use " + MAGENTA + "calculator" + YELLOW + ", age, " + GREEN+"guessing " +RED +"exit?: " + CYAN
    choice = input(menu_prompt).lower().strip()
    
    if choice == "age":
        about()
    elif choice == "calculator" or choice == "calc":
        calcu()
    elif choice =="guess" or choice =="game":
        game()    
    elif choice == "exit" or choice == "q":
        print(GREEN + "bye")
        sys.exit(0)
    else:
        print(YELLOW + "Invalid option, please type calculator, age, or exit.")
        time.sleep(1.5)
