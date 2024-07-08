# login_popup.py

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from popups.kivy_pw_popup.user_manager import validate_user


from kivy.lang import Builder

from constants import IMG_POPUPS

Builder.load_file(IMG_POPUPS + "kivy_pw_popup/popup_log_user.kv")


class LoginPopup(Popup):
    def __init__(self, login_callback, app, **kwargs):
        super(LoginPopup, self).__init__(**kwargs)
        self.login_callback = login_callback
        self.app = app
        self.ids.password_input.focus = True

    def validate_user(self):
        username = self.ids.lab_username.text
        password = self.ids.password_input.text
        if validate_user(username, password):
            self.login_callback(username)
            self.dismiss()
        else:
            self.show_error("Invalid username or password")

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
