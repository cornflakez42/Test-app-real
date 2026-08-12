import random

# Store game state globally within the module
target_number = 0

def start_game():
    global target_number
    target_number = random.randint(1, 100)

def play_turn(user_input):
    global target_number
    try:
        guess = int(user_input)
        if guess < target_number:
            return "Too low! Try a higher number."
        elif guess > target_number:
            return "Too high! Try a lower number."
        else:
            return "Correct! You Won the Game!"
    except ValueError:
        return "Please enter a valid number."
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
