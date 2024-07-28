# login_popup.py

from kivy.uix.popup import Popup

from popups.popup_password.user_manager import PwManager
from popups.pop_info.pop_info import Pop_Info

from kivy.lang import Builder

from constants import DIR_POPUPS

Builder.load_file(DIR_POPUPS + "popup_password/pop_log_user.kv")


class Pop_Login(Popup):
    def __init__(self, app, **kwargs):
        super(Pop_Login, self).__init__(**kwargs)
        self.app = app
        self.pw_man = PwManager(self.app)
        self.ids.password_input.focus = True

    def validate_user(self):
        password = self.ids.password_input.text
        if self.pw_man.validate_user_pw(self.app.user_name, password):
            self.app.login_state = 1
            self.show_info(self.app.lab_txt["status"]["log_succes"])
            self.dismiss()
        else:
            self.show_info(self.app.lab_txt["status"]["inv_uname_or_pw"])

    def show_info(self, message):
        info_popup = Pop_Info(self.app, message)
        info_popup.open()
