import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import age  # type: ignore
import calculator  # type: ignore
import guess_game_numb  # type: ignore


# inside your MyApp class:
def on_submit(self, _instance):
    user_text = self.input_field.text.strip()

    if self.mode == "menu":
        choice = user_text.lower()
        if choice == "age":
            self.mode = "age"
            age.reset_age_state()
            self.title_label.text = "Age Calculator:\nWhat is your name?"
            self.output_label.text = ""
        elif choice in ["calculator", "calc"]:
            self.mode = "calculator"
            calculator.reset_calc_state()
            self.title_label.text = "Calculator:\nEnter your first number:"
            self.output_label.text = ""
        elif choice in ["guess", "game"]:
            self.mode = "guess"
            guess_game_numb.start_game()
            self.title_label.text = "Guessing Game (1-30):\nEnter a number"
            self.output_label.text = "Game started!"
        else:
            self.output_label.text = "Unknown choice, try again."

    elif self.mode == "age":
        msg, sub_state = age.process_age_input(user_text)
        self.output_label.text = msg
        if sub_state == "done":
            self.mode = "menu"
            self.title_label.text = "Choose an Option:\nage, calculator, guess"

    elif self.mode == "calculator":
        msg, sub_state = calculator.process_calculator_input(user_text)
        self.output_label.text = msg
        if sub_state == "done":
            self.mode = "menu"
            self.title_label.text = "Choose an Option:\nage, calculator, guess"

    elif self.mode == "guess":
        try:
            result = guess_game_numb.play_turn(user_text)
            self.output_label.text = str(result)
            if "Correct" in result:
                self.mode = "menu"
                self.title_label.text = "Choose an Option:\nage, calculator, guess"
        except Exception:
            self.output_label.text = "Invalid input! Enter a number."

    self.input_field.text = ""
    
