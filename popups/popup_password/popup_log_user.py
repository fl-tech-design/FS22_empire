# login_popup.py

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from popups.popup_password.user_manager import validate_user


from kivy.lang import Builder

from constants import DIR_POPUPS, DIR_FONTS, TITLEFONT

Builder.load_file(DIR_POPUPS + "popup_password/popup_log_user.kv")


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
            self.show_error()

    def show_error(self):
        error_popup = Popup(
            title=self.app.lab_txt["error"],
            title_size="23sp",
            title_font=DIR_FONTS + TITLEFONT,
            content=Label(
                text=self.app.lab_txt["invalid_username_or_password"],
                font_size=self.height * 0.1,
            ),
            size_hint=(0.3, 0.3),
        )
        error_popup.open()
        Clock.schedule_once(lambda dt: error_popup.dismiss(), 2)
