# login_popup.py

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from popups.popup_password.user_manager import register_user, validate_user

from kivy.lang import Builder

from constants import IMG_POPUPS

Builder.load_file(IMG_POPUPS + "popup_password/popup_reg_user.kv")

class RegisterPopup(Popup):
    def __init__(self, app, **kwargs):
        super(RegisterPopup, self).__init__(**kwargs)
        self.app = app

        Window.bind(on_key_down=self._on_key_down)

    def _on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 43:  # Tab key
            if self.ids.username_input.focus:
                self.ids.password_input.focus = True
            elif self.ids.password_input.focus:
                self.ids.username_input.focus = True
            return True
        return False

    def validate_user(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        if validate_user(username, password):
            self.login_callback(username)
            self.dismiss()
        else:
            self.show_error("Invalid username or password")

    def register_user(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        if register_user(username, password):
            self.show_info("User registered successfully")
            self.app.control_data.remove_empty_list_item(
                self.app.saved_players, username
            )
            self.app.control_data.set_Data_App("saved_players", self.app.saved_players)
            self.app.reload_app_data()
            Clock.schedule_once(lambda dt: self.dismiss(), 1)  # Close after 1 second
        else:
            self.show_error("User already exists")

    def show_error(self, message):
        error_popup = Popup(
            title="Error", content=Label(text=message), size_hint=(0.6, 0.3)
        )
        error_popup.open()
        Clock.schedule_once(lambda dt: error_popup.dismiss(), 1)  # Close after 1 second

    def show_info(self, message):
        info_popup = Popup(
            title="Info", content=Label(text=message), size_hint=(0.6, 0.3)
        )
        info_popup.open()
        Clock.schedule_once(lambda dt: info_popup.dismiss(), 1)  # Close after 1 second
