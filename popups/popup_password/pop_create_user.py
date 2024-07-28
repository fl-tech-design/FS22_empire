# Pop_Create_User

from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from popups.popup_password.user_manager import PwManager
from popups.pop_info.pop_info import Pop_Info
from kivy.lang import Builder
from datetime import datetime

import json

from control_data import DataControl

from constants import DIR_POPUPS, PATH_DIR_U_DAT

Builder.load_file(DIR_POPUPS + "popup_password/pop_create_user.kv")


class Pop_Create_User(Popup):
    def __init__(self, app, **kwargs):
        super(Pop_Create_User, self).__init__(**kwargs)
        self.app = app
        self.pw_man = PwManager(self.app)
        self.ids.u_name_input.focus = True
        Window.bind(on_key_down=self._on_key_down)

    def _on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 43:  # Tab key
            if self.ids.u_name_input.focus:
                self.ids.pw_input.focus = True
            elif self.ids.pw_input.focus:
                self.ids.u_name_input.focus = True
            return True
        return False

    def reg_user_but_pressed(self):
        u_name = self.ids.u_name_input.text
        pw = self.ids.pw_input.text
        reg_state = self.is_user_registered(u_name)
        if reg_state:
            pop_inf = Pop_Info(
                self.app, self.app.lab_txt["descr"]["descr_is_registered_username"]
            )
            pop_inf.open()
        else:
            self.add_uname_to_ulist(u_name)
            self.create_User_File(u_name, pw)
            self.app.reload_app_data()
            self.dismiss()

    # 27.07.24
    def is_user_registered(self, uname: str) -> bool:
        """
        Checks if a user is registered in the app's user list.

        Args:
            uname (str): The username to check.

        Returns:
            bool: True if the user is registered, otherwise False.
        """

        return uname in self.app.user_list

    def add_uname_to_ulist(self, new_uname):
        try:
            # Ersetzt den ersten leeren Platzhalter durch den neuen String
            index = self.app.user_list.index("")
            self.app.user_list[index] = new_uname
            DataControl.set_Uname_List(self, index, new_uname)
        except ValueError:
            # Falls keine Platzhalter mehr vorhanden sind, füge den neuen String am Ende der Liste hinzu
            self.app.user_list.append(new_uname)

    def create_User_File(self, uname: str, pw: str) -> None:
        now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        new_user_data = {
            "uname": uname,
            "password": self.pw_man.hash_password(pw),
            "crea_date": now,
            "last_login": now,
            "sa_games": "0",
            "pl_games": "0",
            "last_game": "",
            "tot_p_time": "00:00",
            "s_g_names": ["", "", "", "", ""],
            "sa_games_data": ["", "", "", "", ""],
            "curr_g_name": "",
            "curr_game_data": {
                "map_name": "",
                "curr_player": "",
                "tot_p_time": "0",
                "number_of_sa_games": 0,
                "last_save": "",
                "days_per_month": 1,
                "time_scale": 5,
            },
        }
        try:
            with open(f"{PATH_DIR_U_DAT}{uname}.json", "w") as file:
                json.dump(new_user_data, file)
        except FileNotFoundError as f_err:
            DataControl.log_error(f_err)
        except json.JSONDecodeError as dec_err:
            DataControl.log_error(dec_err)
        except Exception as exp_err:
            DataControl.log_error(exp_err)

    def show_info(self, message):
        info_popup = Pop_Info(self.app, message)
        info_popup.open()
