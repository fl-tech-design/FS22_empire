# popup_new_user.py

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty
from kivy.core.window import Window
import json
import os


class Popup_New_User(Popup):
    def __init__(self, lab_txt, app, **kwargs):
        super().__init__(**kwargs)
        self.txt_lab = lab_txt

        self.title = self.txt_lab['new_player']
        self.size_hint = (0.25, 0.25)
        
        Window.borderless = '1'

        # Layouts
        layout = BoxLayout(orientation='vertical')
        form_layout = GridLayout(cols=2)
        form_layout.spacing = 10
        self.lab_uname = Label(text=self.txt_lab['username'])
        self.inp_uname = TextInput(multiline=False, font_size=self.height * 0.3, padding=3)
        self.lab_passwd = Label(text=self.txt_lab['password'])
        self.inp_passwd = TextInput(multiline=False, password=True, font_size=self.height * 0.3, padding=3)

        form_layout.add_widget(self.lab_uname)
        form_layout.add_widget(self.inp_uname)
        form_layout.add_widget(self.lab_passwd)
        form_layout.add_widget(self.inp_passwd)

        layout.add_widget(form_layout)

        # Buttons
        button_layout = BoxLayout(size_hint_y=0.2)
        save_button = Button(text=self.txt_lab['save'])
        cancel_button = Button(text=self.txt_lab['cancel'])

        save_button.bind(on_release=self.save_data)
        cancel_button.bind(on_release=self.dismiss)

        button_layout.add_widget(save_button)
        button_layout.add_widget(cancel_button)

        layout.add_widget(button_layout)

        self.add_widget(layout)
        Window.bind(on_key_down=self._on_key_down)

    def _on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 43 or keycode == 40:  # Tab key
            if self.inp_uname.focus:
                self.inp_passwd.focus = True
            elif self.inp_passwd.focus:
                self.inp_uname.focus = True
            return True
        return False

    def save_data(self, instance):
        data = {
            self.lab_uname.text: self.inp_uname.text,
            self.lab_passwd.text: self.inp_passwd.text,
        }

        # Load existing data with error handling
        existing_data = {}
        if os.path.exists("files_data/data_users.json"):
            try:
                with open("files_data/data_users.json", "r") as f:
                    existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {}

        # Determine new vehicle ID
        new_id = self.inp_uname.text
        # Add new data to existing data
        existing_data[new_id] = data

        # Save updated data
        with open("files_data/data_users.json", "w") as f:
            json.dump(existing_data, f, indent=4)

        self.dismiss()
