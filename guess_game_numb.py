import random
import os
import time

# color
WHITE = "\033[1;37m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"

# new function guessing game
def game():
    randomnumb = random.randint(0, 30)
    attempts = 0
    
    # Start the timer using standard Python time
    start_time = time.time()

    while True:
        print(CYAN + "guess the number between 1 - 30/ debug = ", randomnumb)
        
        try:
            guess = int(input(CYAN + "enter your guess "))
        except ValueError:
            print("please enter number")
            print("")
            continue

        print("")
        attempts += 1
        os.system("clear")

        if guess < randomnumb:
            print("too low try again ")
            print("debug num trys", WHITE, attempts)
            print("")
        elif guess > randomnumb:
            print("too high try again ")
            print("debug num trys", WHITE, attempts)
            print("")
        elif guess < 0:
            print("try again")
        elif guess == randomnumb:
            # Calculate total time taken
            end_time = time.time()
            seconds_taken = round(end_time - start_time, 1)
            
            print("")
            print("congrats well done it took you ", attempts, " atempts!")
            print("You solved it in", seconds_taken, "seconds!")
            print("")
            
            option = input("Would you like to return home or try again? ")
            if option == "again" or option == "a" or option == "try":
                game()
                return
            else:
                break
			continue

		print("")
		attempts += 1
		os.system("clear")

		if guess < randomnumb:
			print("too low try again ")
			# debug
			print("debug num trys", WHITE, attempts)
			# end debug
			print("")
		elif guess > randomnumb:
			print("too high try again ")
			# debug
			print("debug num trys", WHITE, attempts)
			# end debug
			print("")
		elif guess < 0:
			print("try again")
		elif guess == randomnumb:
			# Convert the total milliseconds tracked into clean seconds
			seconds_taken = round(total_time_ms / 1000, 1)
			
			print("")
			print("congrats well done it took you ", attempts, " atempts!")
			print("You solved it in", seconds_taken, "seconds!")
			print("")
			
			option = input("Would you like to return home or try again? ")
			if option == "again" or option == "a" or option == "try":
				game()
				return
			else:
				break

# end game function
