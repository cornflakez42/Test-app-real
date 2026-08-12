import random
import time

# Store game state globally within the module
target_number = 0
attempts = 0
start_time = 0

def start_game():
    global target_number, attempts, start_time
    target_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

def play_turn(user_input):
    global target_number, attempts
    try:
        guess = int(user_input)
        attempts += 1
        
        if guess < 0:
            return "Please enter a positive number."
        elif guess < target_number:
            return "Too low! Try a higher number."
        elif guess > target_number:
            return "Too high! Try a lower number."
        else:
            end_time = time.time()
            seconds_taken = round(end_time - start_time, 1)
            return f"Correct! You won in {attempts} attempts and {seconds_taken} seconds!"
    except ValueError:
        return "Please enter a valid number."
