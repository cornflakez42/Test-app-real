from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#cmcadam
import age
import calculator
import guess_game_numb

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.title_label = Label(
            text="Choose an Option: age, calculator, guess",
            font_size=18,
            halign='center',
            valign='middle'
        )
        self.layout.add_widget(self.title_label)
        
        self.input_field = TextInput(
            text='',
            hint_text='Type your choice or value here',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.layout.add_widget(self.input_field)
        
        self.submit_btn = Button(
            text='Submit',
            size_hint_y=None,
            height=60
        )
        self.submit_btn.bind(on_press=self.on_submit)
        self.layout.add_widget(self.submit_btn)
        
        self.output_label = Label(
            text='',
            font_size=16,
            halign='center'
        )
        self.layout.add_widget(self.output_label)
        
        # Keep track of active mode ("menu", "age", "calculator", "guess")
        self.mode = "menu"
        return self.layout

    def on_submit(self, instance):
        user_text = self.input_field.text.strip()
        
        if self.mode == "menu":
            choice = user_text.lower()
            if choice == "age":
                self.mode = "age"
                self.title_label.text = "Age Calculator: Enter your birth year"
                self.output_label.text = ""
            elif choice in ["calculator", "calc"]:
                self.mode = "calculator"
                self.title_label.text = "Calculator: Enter an expression (e.g., 5 + 5)"
                self.output_label.text = ""
            elif choice in ["guess", "game", "guess game"]:
                self.mode = "guess"
                guess_game_numb.start_game()
                self.title_label.text = "Guessing Game: Enter a number (1-100)"
                self.output_label.text = "Game started! Make a guess."
            else:
                self.output_label.text = "Unknown choice, try again."
                
        elif self.mode == "age":
            result = age.calculate_age(user_text)
            self.output_label.text = result
            self.mode = "menu"
            self.title_label.text = "Choose an Option: age, calculator, guess"
            
        elif self.mode == "calculator":
            result = calculator.calculate(user_text)
            self.output_label.text = result
            self.mode = "menu"
            self.title_label.text = "Choose an Option: age, calculator, guess"
            
        elif self.mode == "guess":
            result = guess_game_numb.play_turn(user_text)
            self.output_label.text = result
            if "Won" in result or "Correct" in result:
                self.mode = "menu"
                self.title_label.text = "Choose an Option: age, calculator, guess"
                
        self.input_field.text = ""

if __name__ == '__main__':
    MyApp().run()
            height=60
        )
        # Properly bound to the on_submit function
        self.submit_btn.bind(on_press=self.on_submit)

        self.layout.add_widget(self.submit_btn)
        
        self.output_label = Label(text='')
        self.layout.add_widget(self.output_label)
        
        return self.layout

    def on_submit(self, instance):
        # .strip() removes accidental leading/trailing spaces from mobile typing
        choice = self.input_field.text.strip().lower()
        
        if choice == "age":
            self.output_label.text = "Age calculator selected."
            # Uncomment below once your age.py has a starting function
            # age.main()
            
        elif choice in ["calculator", "calc"]:
            self.output_label.text = "Calculator selected."
            # Uncomment below once your calculator.py has a starting function
            # calculator.main()
            
        elif choice in ["guess", "game", "guess game"]:
            self.output_label.text = "Guessing game selected."
            # Uncomment below once your guess_game_numb.py has a starting function
            # guess_game_numb.main()
            
        else:
            self.output_label.text = "Unknown choice, try again."

if __name__ == '__main__':
    MyApp().run()
