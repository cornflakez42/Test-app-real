from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.utils import platform

# Import Android wake lock modules if running on an Android device
if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    WindowManager = autoclass('android.view.WindowManager$LayoutParams')

import age
import calculator
import guess_game_numb

class MyApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical')
        
        self.content_box = BoxLayout(
            orientation='vertical',
            spacing=dp(20),
            size_hint=(None, None),
            width=dp(320),
            height=dp(360),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        self.title_label = Label(
            text="Choose an Option:\nage, calculator, guess",
            font_size=dp(20),
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=dp(80)
        )
        self.title_label.bind(size=lambda s, w: setattr(s, 'text_size', w))
        self.content_box.add_widget(self.title_label)
        
        self.input_field = TextInput(
            text='',
            hint_text='Type choice or value',
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )
        self.content_box.add_widget(self.input_field)
        
        self.submit_btn = Button(
            text='Submit',
            size_hint_y=None,
            height=dp(60)
        )
        self.submit_btn.bind(on_press=self.on_submit)
        self.content_box.add_widget(self.submit_btn)
        
        self.output_label = Label(
            text='',
            font_size=dp(18),
            halign='center',
            size_hint_y=None,
            height=dp(60)
        )
        self.output_label.bind(size=lambda s, w: setattr(s, 'text_size', w))
        self.content_box.add_widget(self.output_label)
        
        root_layout.add_widget(self.content_box)
        
        self.mode = "menu"
        return root_layout

    def on_start(self):
        # Keep screen awake while the app is running on Android
        if platform == 'android':
            try:
                activity = PythonActivity.mActivity
                activity.runOnUiThread(Runnable({
                    'run': lambda: activity.getWindow().addFlags(WindowManager.FLAG_KEEP_SCREEN_ON)
                }))
            except Exception as e:
                print(f"Wake lock error: {e}")

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
                self.title_label.text = "Calculator:\nEnter expression (e.g. 5+5)"
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
