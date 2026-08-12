import sys
import os
import traceback

try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    import age  # type: ignore
    import calculator  # type: ignore
    import guess_game_numb  # type: ignore

    import kivy
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.label import Label
    from kivy.uix.textinput import TextInput
    from kivy.uix.button import Button

    class MyApp(App):
        def build(self):
            self.mode = "menu"

            # Outer ScrollView allows the screen to adapt when the keyboard pops up
            scroll = ScrollView(do_scroll_x=False)

            # Inner layout uses a flexible height layout centered vertically
            root = BoxLayout(
                orientation="vertical",
                padding=30,
                spacing=20,
                size_hint_y=None,
                size_hint_x=1,
            )
            root.bind(minimum_height=root.setter("height"))

            # Spacer to push contents toward the center
            top_spacer = BoxLayout(size_hint_y=None, height=50)
            root.add_widget(top_spacer)

            self.title_label = Label(
                text="Choose an Option:\nage, calculator, guess",
                font_size="22sp",
                size_hint_y=None,
                height=120,
                halign="center",
                valign="middle",
            )
            self.title_label.bind(size=self.title_label.setter("text_size"))
            root.add_widget(self.title_label)

            self.output_label = Label(
                text="",
                font_size="20sp",
                size_hint_y=None,
                height=150,
                halign="center",
                valign="middle",
            )
            self.output_label.bind(size=self.output_label.setter("text_size"))
            root.add_widget(self.output_label)

            self.input_field = TextInput(
                text="",
                multiline=False,
                size_hint_y=None,
                height=60,
                font_size="22sp",
                halign="center",
            )
            root.add_widget(self.input_field)

            submit_btn = Button(
                text="Submit", size_hint_y=None, height=60, font_size="22sp"
            )
            submit_btn.bind(on_press=self.on_submit)
            root.add_widget(submit_btn)

            scroll.add_widget(root)
            return scroll

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
                        self.title_label.text = (
                            "Choose an Option:\nage, calculator, guess"
                        )
                except Exception:
                    self.output_label.text = "Invalid input! Enter a number."

            self.input_field.text = ""

    if __name__ == "__main__":
        MyApp().run()

except Exception as e:
    error_file = "/storage/emulated/0/Download/crash_log.txt"
    with open(error_file, "w") as f:
        f.write(traceback.format_exc())
    raise e
