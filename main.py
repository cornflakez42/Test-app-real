import os
import sys
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

      scroll = ScrollView(do_scroll_x=False)

      root = BoxLayout(
          orientation="vertical",
          padding=30,
          spacing=20,
          size_hint_y=None,
          size_hint_x=1,
      )
      root.bind(minimum_height=root.setter("height"))

      top_spacer = BoxLayout(size_hint_y=None, height=30)
      root.add_widget(top_spacer)

      self.title_label = Label(
          text="Choose an Option:\nage, calculator, guess",
          font_size="20sp",
          size_hint_y=None,
          halign="center",
          valign="middle",
      )
      self.title_label.bind(
          width=lambda *x: setattr(
              self.title_label, "text_size", (self.title_label.width, None)
          ),
          texture_size=lambda *x: setattr(
              self.title_label, "height", self.title_label.texture_size[1]
          ),
      )
      root.add_widget(self.title_label)

      self.output_label = Label(
          text="",
          font_size="18sp",
          size_hint_y=None,
          halign="center",
          valign="middle",
      )
      self.output_label.bind(
          width=lambda *x: setattr(
              self.output_label, "text_size", (self.output_label.width, None)
          ),
          texture_size=lambda *x: setattr(
              self.output_label, "height", self.output_label.texture_size[1]
          ),
      )
      root.add_widget(self.output_label)

      self.input_field = TextInput(
          text="",
          multiline=False,
          size_hint_y=None,
          height=50,
          font_size="20sp",
          halign="left",
          padding_x=[10, 10],
          padding_y=[12, 12],
      )
      root.add_widget(self.input_field)

      submit_btn = Button(
          text="Submit", size_hint_y=None, height=55, font_size="20sp"
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
        if sub_state == "done":
          self.output_label.text = msg
          self.title_label.text = "Finished! (Press Submit for menu)"
          self.mode = "menu_reset"
        else:
          self.output_label.text = ""
          self.title_label.text = msg

      elif self.mode == "calculator":
        msg, sub_state = calculator.process_calculator_input(user_text)
        if sub_state == "done":
          self.output_label.text = msg
          self.title_label.text = "Result: (Press Submit for menu)"
          self.mode = "menu_reset"
        else:
          self.output_label.text = ""
          self.title_label.text = msg

      elif self.mode == "menu_reset":
        self.mode = "menu"
        self.title_label.text = "Choose an Option:\nage, calculator, guess"
        self.output_label.text = ""

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


  if __name__ == "__main__":
    MyApp().run()

except Exception as e:
  error_file = "/storage/emulated/0/Download/crash_log.txt"
  with open(error_file, "w") as f:
    f.write(traceback.format_exc())
  raise e
