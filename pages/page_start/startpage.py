# startpage.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from constants import *

from popups.popup_password.pop_create_user import Pop_Create_User
from popups.popup_password.pop_log_user import Pop_Login

from control_data import DataControl

Builder.load_file(PATH_KV_STARTPAGE)


class StartPageUpdater:
    def __init__(self, app, ids):
        self.app = app
        self.ids = ids
        self.ids.box_bottom.ids.but_1.bind(on_release=lambda dt: self.app.change_Screen("left", "page_settings"))

    def update(self):
        self.upd_box_title()
        self.upd_box_reg_user()
        self.upd_box_user_info()
        self.upd_box_g_saves()
        self.upd_lab_buttons()

    def upd_box_title(self):
        self.ids.box_tit.ids.lab_tit.text = self.app.lab_txt["app"]["page_start"]

    def upd_box_reg_user(self):
        self.ids.lab_reg_users.text = f'{self.app.lab_txt["app"]["reg_users"]}'
        for i in range(5):
            self.ids[f"but_uname_{i + 1}"].text = (
                self.app.user_list[i] if i < len(self.app.user_list) else ""
            )

    def upd_box_user_info(self):
        user_data = self.app.user_data if self.app.user_name else {}
        self.ids.box_u_info.ids.lab_tit_user_info.text = (
            f'{self.app.lab_txt["app"]["user_data"]}: {self.app.user_name}'
        )
        self.ids.box_u_info.ids.lab_r0_c0.text = self.app.lab_txt["app"][
            "crea_date"
        ].split()[1]
        self.ids.box_u_info.ids.lab_r1_c0.text = self.app.lab_txt["app"]["last_login"]
        self.ids.box_u_info.ids.lab_r2_c0.text = self.app.lab_txt["app"]["sa_games"]
        self.ids.box_u_info.ids.lab_r3_c0.text = self.app.lab_txt["app"]["pl_games"]
        self.ids.box_u_info.ids.lab_r4_c0.text = self.app.lab_txt["app"]["last_game"]
        self.ids.box_u_info.ids.lab_r5_c0.text = self.app.lab_txt["app"]["tot_p_time"]

        if self.app.login_state:
            self.ids.box_u_info.ids.lab_r0_c1.text = user_data.get("crea_date", "")
            self.ids.box_u_info.ids.lab_r1_c1.text = user_data.get("last_login", "")
            self.ids.box_u_info.ids.lab_r2_c1.text = f'{user_data.get("sa_games", "")}'
            self.ids.box_u_info.ids.lab_r3_c1.text = f'{user_data.get("pl_games", "")}'
            self.ids.box_u_info.ids.lab_r4_c1.text = user_data.get("last_game", "")
            self.ids.box_u_info.ids.lab_r5_c1.text = user_data.get("tot_p_time", "")
        else:
            for i in range(6):
                self.ids.box_u_info.ids[f"lab_r{i}_c1"].text = ""

    def upd_box_g_saves(self):
        # labeltext of boxtitle: Savegames
        self.ids.lab_tit_g_saves.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["g_saves"].split()[1]
        )
        # set images of saved games. only set if a user set.
        if self.app.user_name:
            for i in range(1, 6):

                if self.app.user_data["s_g_names"][i - 1]:
                    self.ids[f"box_sg_{i}"].ids.img_map.source = f"saved game 1 image"
                    self.ids[f"box_sg_{i}"].ids.l_img_map.text = ""
                    self.ids[f"box_sg_{i}"].ids.b_load_game.text = self.app.lab_txt[
                        "app"
                    ]["start_game"]
                    self.ids[f"box_sg_{i}"].ids.b_del_game.disabled = False
                self.ids[f"box_sg_{i}"].ids.b_load_game.disabled = False
        else:
            for i in range(1, 6):
                self.ids[f"box_sg_{i}"].ids.img_map.source = f"{BUT_CLEAR}"
                self.ids[f"box_sg_{i}"].ids.l_img_map.text = (
                    f'{self.app.lab_txt["phrases"]["free_place"]}'
                )
                self.ids[f"box_sg_{i}"].ids.b_load_game.text = self.app.lab_txt["app"][
                    "new_game"
                ]
                self.ids[f"box_sg_{i}"].ids.b_del_game.disabled = True
                self.ids[f"box_sg_{i}"].ids.b_load_game.disabled = True
        # set labeltext of delet button
        for i in range(1, 6):
            self.ids[f"box_sg_{i}"].ids.b_del_game.text = self.app.f_let_upper(
                self.app.lab_txt["verbs"]["delete"]
            )

    def upd_lab_buttons(self):
        self.ids.but_logout_user.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["logout"]
        )
        self.ids.but_new_user.text = self.app.lab_txt["app"]["new_player"]

        self.ids.box_bottom.ids.but_1.text = self.app.lab_txt["settings"]["settings"]
        self.ids.box_bottom.ids.but_2.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["quit"]
        )


class StartPage(Screen):
    def __init__(self, app, scr_man, **kwargs):
        super(StartPage, self).__init__(**kwargs)
        self.app = app
        self.scr_man = scr_man
        self.contr_data = DataControl(self.app)

        self.set_But_Names()
        for i in range(1, 6):  # Gehe von 1 bis 5, entsprechend den Box-IDs
            box_id = f"box_sg_{i}"
            button = self.ids[box_id].ids.b_load_game
            button.bind(
                on_release=lambda dt, btn=button: self.but_Load_Game_Pressed(
                    btn.name,
                    btn.text,
                )
            )

    def update_page_start(self):
        self.set_But_State()
        updater = StartPageUpdater(self.app, self.ids)
        updater.update()

    def set_But_State(self) -> None:
        for i in range(5):
            button_id = f"but_uname_{i + 1}"
            button = self.ids[button_id]
            button.disabled = not self.app.user_list[i]
        self.ids.but_logout_user.disabled = not self.app.user_name

    def userbut_Pressed(self, but_uname_text: str) -> None:
        self.app.user_name = but_uname_text
        self.app.user_data = self.contr_data.load_User_Data(self.app.user_name)
        pop = Pop_Login(self.app)
        pop.open()
        



    def but_Load_Game_Pressed(self, name, txt):
        if name == "b_gs_1_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game(self.scr_man)
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player]["sa_games_data"][0]
                )
        elif name == "b_gs_2_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game(self.scr_man)
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player]["sa_games_data"][1]
                )
        elif name == "b_gs_3_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game(self.scr_man)
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player]["sa_games_data"][2]
                )
        elif name == "b_gs_4_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game(self.scr_man)
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player]["sa_games_data"][3]
                )
        elif name == "b_gs_5_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game(self.scr_man)
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player]["sa_games_data"][4]
                )

    def set_But_Names(self):
        self.ids.box_sg_1.ids.b_load_game.name = "b_gs_1_start"
        self.ids.box_sg_2.ids.b_load_game.name = "b_gs_2_start"
        self.ids.box_sg_3.ids.b_load_game.name = "b_gs_3_start"
        self.ids.box_sg_4.ids.b_load_game.name = "b_gs_4_start"
        self.ids.box_sg_5.ids.b_load_game.name = "b_gs_5_start"

    def create_New_User(self):
        popup = Pop_Create_User(self.app)
        popup.open()

    def logout_User(self):
        self.app.curr_player = ""
        self.app.login_state = 0
