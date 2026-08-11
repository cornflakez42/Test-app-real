from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.title_label = Label(
            text="Choose an Option:\n1. Calculator\n2. Age Calculator\n3. Guessing Game",
            font_size=20,
            halign='center',
            valign='middle'
        )
        self.layout.add_widget(self.title_label)
        
        self.input_field = TextInput(
            text='', 
            hint_text='Type calc, age, or guess...', 
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
        
        self.output_label = Label(text='', font_size=18)
        self.layout.add_widget(self.output_label)
        
        return self.layout

    def on_submit(self, instance):
        choice = self.input_field.text.lower().strip()
        if choice == "age":
            self.output_label.text = "Age calculator selected. (Modular UI ready)"
        elif choice == "calculator" or choice == "calc":
            self.output_label.text = "Calculator selected. (Modular UI ready)"
        elif choice == "guess" or choice == "game":
            self.output_label.text = "Guessing game selected. (Modular UI ready)"
        else:
            self.output_label.text = "Invalid choice! Type calc, age, or guess."

if __name__ == '__main__':
    MainApp().run()
    else:
        print(YELLOW + "Invalid option, please type calculator, age, guess, or exit.")
        time.sleep(1.5)
