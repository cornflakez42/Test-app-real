import random
import time

# Store game state globally within the module
target_number = 0
attempts = 0
start_time = 0

def start_game():
    global target_number, attempts, start_time
    target_number = random.randint(1, 30)
    attempts = 0
    start_time = time.time()

def play_turn(user_input):
    global target_number, attempts
    try:
        guess = int(user_input)
        attempts += 1
        
        if guess < 0:
            return f"[DEBUG: {target_number}] Please enter a positive number."
        elif guess < target_number:
            return f"[DEBUG: {target_number}] Too low! Try a higher number."
        elif guess > target_number:
            return f"[DEBUG: {target_number}] Too high! Try a lower number."
        else:
            end_time = time.time()
            seconds_taken = round(end_time - start_time, 2)
            return f"[DEBUG: {target_number}] Correct! You won in {attempts} attempts in {seconds_taken}s."
            
    except ValueError:
        return "Please enter a valid number."
        
