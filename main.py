from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import age
import calculator
import guess_game_numb

class MyApp(App):
    def build(self):
        # Root layout fills the screen and centers content vertically
        root_layout = BoxLayout(
            orientation='vertical', 
            padding=20, 
            spacing=15
        )
        
        # Inner container for UI elements so they don't stretch fullscreen
        self.content_box = BoxLayout(
            orientation='vertical',
            spacing=15,
            size_hint_y=None,
            height=320
        )
        
        self.title_label = Label(
            text="Choose an Option:\nage, calculator, guess",
            font_size=18,
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=80
        )
        # Ensure text wraps or centers nicely in the label box
        self.title_label.bind(
            size=lambda s, w: setattr(s, 'text_size', w)
        )
        self.content_box.add_widget(self.title_label)
        
        self.input_field = TextInput(
            text='',
            hint_text='Type your choice or value here',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.content_box.add_widget(self.input_field)
        
        self.submit_btn = Button(
            text='Submit',
            size_hint_y=None,
            height=60
        )
        self.submit_btn.bind(on_press=self.on_submit)
        self.content_box.add_widget(self.submit_btn)
        
        self.output_label = Label(
            text='',
            font_size=16,
            halign='center',
            size_hint_y=None,
            height=60
        )
        self.output_label.bind(
            size=lambda s, w: setattr(s, 'text_size', w)
        )
        self.content_box.add_widget(self.output_label)
        
        # Add the compact content box into the center of the root layout
        root_layout.add_widget(self.content_box)
        
        # Keep track of active mode ("menu", "age", "calculator", "guess")
        self.mode = "menu"
        return root_layout

    def on_submit(self, instance):
        user_text = self.input_field.text.strip()
        
        if self.mode == "menu":
            choice = user_text.lower()
            if choice == "age":
                self.mode = "age"
                self.title_label.text = "Age Calculator:\nEnter your birth year"
                self.output_label.text = ""
            elif choice in ["calculator", "calc"]:
                self.mode = "calculator"
                self.title_label.text = "Calculator:\nEnter an expression (e.g., 5 + 5)"
                self.output_label.text = ""
            elif choice in ["guess", "game", "guess game"]:
                self.mode = "guess"
                guess_game_numb.start_game()
                self.title_label.text = "Guessing Game:\nEnter a number (1-100)"
                self.output_label.text = "Game started! Make a guess."
            else:
                self.output_label.text = "Unknown choice, try again."
                
        elif self.mode == "age":
            result = age.calculate_age(user_text)
            self.output_label.text = result
            self.mode = "menu"
            self.title_label.text = "Choose an Option:\nage, calculator, guess"
            
        elif self.mode == "calculator":
            result = calculator.calculate(user_text)
            self.output_label.text = result
            self.mode = "menu"
            self.title_label.text = "Choose an Option:\nage, calculator, guess"
            
        elif self.mode == "guess":
            result = guess_game_numb.play_turn(user_text)
            self.output_label.text = result
            if "Won" in result or "Correct" in result:
                self.mode = "menu"
                self.title_label.text = "Choose an Option:\nage, calculator, guess"
                
        self.input_field.text = ""

if __name__ == '__main__':
    MyApp().run()
    
