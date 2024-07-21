from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from constants import *

from popups.popup_password.user_manager import load_user_data
from popups.popup_select_map.popup_sel_map import PopupSelectMap

Builder.load_file(PATH_KV_STARTPAGE)


class StartPageUpdater:
    def __init__(self, app, ids):
        self.app = app
        self.ids = ids

    def update(self):
        self.upd_box_title()
        self.upd_box_reg_user()
        self.upd_box_user_info()
        self.upd_box_g_saves()
        self.update_buttons()

    def upd_box_title(self):
        self.ids.box_tit.ids.lab_tit.text = self.app.lab_txt["app"]["page_start"]

    def upd_box_reg_user(self):
        self.ids.lab_reg_users.text = f'{self.app.lab_txt["app"]["registered_users"]}'
        for i in range(5):
            self.ids[f"but_uname_{i + 1}"].text = (
                self.app.saved_players[i] if i < len(self.app.saved_players) else ""
            )

    def upd_box_user_info(self):
        user_data = self.app.curr_u_data if self.app.curr_player else {}
        self.ids.box_u_info.ids.lab_tit_user_info.text = (
            f'{self.app.lab_txt["app"]["user_data"]}: {self.app.curr_player}'
        )
        self.ids.box_u_info.ids.lab_r0_c0.text = self.app.lab_txt["app"][
            "crea_date"
        ].split()[1]
        self.ids.box_u_info.ids.lab_r1_c0.text = self.app.lab_txt["app"]["last_login"]
        self.ids.box_u_info.ids.lab_r2_c0.text = self.app.lab_txt["app"]["sa_games"]
        self.ids.box_u_info.ids.lab_r3_c0.text = self.app.lab_txt["app"]["pl_games"]
        self.ids.box_u_info.ids.lab_r4_c0.text = self.app.lab_txt["app"]["last_game"]
        self.ids.box_u_info.ids.lab_r5_c0.text = self.app.lab_txt["app"]["tot_p_time"]

        if self.app.curr_player:
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
        # load userdata
        user_data = load_user_data()
        # labeltext of boxtitle: Savegames
        self.ids.lab_tit_g_saves.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["sa_games"]
        )
        # set images of saved games. only set if a user set.
        if self.app.curr_player:
            for i in range(1, 6):
                if self.app.curr_u_data["s_g_names"][i - 1]:
                    self.ids[f"box_sg_{i}"].ids.img_map.source = (
                        f'{DIR_SPLASH_SCR}{self.app.data_app["maps"][user_data[self.app.curr_player]["s_g_names"][i - 1]]["img_spl_scr"]}'
                    )
                    self.ids[f"box_sg_{i}"].ids.l_img_map.text = ""
                    self.ids[f"box_sg_{i}"].ids.b_load_game.text = self.app.lab_txt["app"][
                        "start_game"
                    ]
                    self.ids[f"box_sg_{i}"].ids.b_del_game.disabled = False
                self.ids[f"box_sg_{i}"].ids.b_load_game.disabled = False
        else:
            for i in range(1, 6):
                self.ids[f"box_sg_{i}"].ids.img_map.source = f"{BUT_CLEAR}"
                self.ids[f"box_sg_{i}"].ids.l_img_map.text = f"freier Platz"
                self.ids[f"box_sg_{i}"].ids.b_load_game.text = self.app.lab_txt["app"][
                    "new_game"
                ]
                self.ids[f"box_sg_{i}"].ids.b_del_game.disabled = True
                self.ids[f"box_sg_{i}"].ids.b_load_game.disabled = True
        #set labeltext of delet button
        for i in range(1, 6):
            self.ids[f"box_sg_{i}"].ids.b_del_game.text = self.app.f_let_upper(
                self.app.lab_txt["verbs"]["delete"]
            )


    def update_buttons(self):
        self.ids.but_logout_user.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["logout"]
        )
        self.ids.but_new_user.text = self.app.lab_txt["app"]["new_player"]


        self.ids.box_bottom.ids.but_1.text = self.app.lab_txt["settings"][
            "settings"
        ]
        self.ids.box_bottom.ids.but_2.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["quit"]
        )


class StartPage(Screen):
    def __init__(self, app, scr_man, **kwargs):
        super(StartPage, self).__init__(**kwargs)
        self.app = app
        self.scr_man = scr_man
        self.state_game_selected = 0
        self.state_user_selected = 0
        self.set_But_Names()
        self.ids.box_sg_1.ids.b_load_game.bind(
            on_release=lambda dt: self.but_Load_Game_Pressed(
                self.ids.box_sg_1.ids.b_load_game.name,
                self.ids.box_sg_1.ids.b_load_game.text,
            )
        )
        self.ids.box_sg_2.ids.b_load_game.bind(
            on_release=lambda dt: self.but_Load_Game_Pressed(
                self.ids.box_sg_2.ids.b_load_game.name,
                self.ids.box_sg_2.ids.b_load_game.text,
            )
        )
        self.ids.box_sg_3.ids.b_load_game.bind(
            on_release=lambda dt: self.but_Load_Game_Pressed(
                self.ids.box_sg_3.ids.b_load_game.name,
                self.ids.box_sg_3.ids.b_load_game.text,
            )
        )
        self.ids.box_sg_4.ids.b_load_game.bind(
            on_release=lambda dt: self.but_Load_Game_Pressed(
                self.ids.box_sg_4.ids.b_load_game.name,
                self.ids.box_sg_4.ids.b_load_game.text,
            )
        )
        self.ids.box_sg_5.ids.b_load_game.bind(
            on_release=lambda dt: self.but_Load_Game_Pressed(
                self.ids.box_sg_5.ids.b_load_game.name,
                self.ids.box_sg_5.ids.b_load_game.text,
            )
        )
        Clock.schedule_once(self.app.update_app_loop, 4)

    def update_page_start(self):
        self.set_But_State()
        updater = StartPageUpdater(self.app, self.ids)
        updater.update()

        
    def set_But_State(self):
        # usernamebuttons
        if self.app.saved_players[0]:
            self.ids.but_uname_1.disabled = False
        else:
            self.ids.but_uname_1.disabled = True
        if self.app.saved_players[1]:
            self.ids.but_uname_2.disabled = False
        else:
            self.ids.but_uname_2.disabled = True
        if self.app.saved_players[2]:
            self.ids.but_uname_3.disabled = False
        else:
            self.ids.but_uname_3.disabled = True
        if self.app.saved_players[3]:
            self.ids.but_uname_4.disabled = False
        else:
            self.ids.but_uname_4.disabled = True
        if self.app.saved_players[4]:
            self.ids.but_uname_5.disabled = False
        else:
            self.ids.but_uname_5.disabled = True
        # logoutbutton state
        if self.app.curr_player:
            self.ids.but_logout_user.disabled = False
        else:
            self.ids.but_logout_user.disabled = True

    def set_User(self, curr_uname):
        self.app.curr_u_name = curr_uname
        self.app.open_login_popup()
        self.app.login_state = 1
        self.app.saved_game_data_from_curr_player = load_user_data()

    def but_Load_Game_Pressed(self, name, txt):
        if name == "b_gs_1_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game(self.scr_man)
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player][
                        "sa_games_data"
                    ][0]
                )
        elif name == "b_gs_2_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game()
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player][
                        "sa_games_data"
                    ][1]
                )
        elif name == "b_gs_3_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game()
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player][
                        "sa_games_data"
                    ][2]
                )
        elif name == "b_gs_4_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game()
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player][
                        "sa_games_data"
                    ][3]
                )
        elif name == "b_gs_5_start":
            if txt == self.app.lab_txt["app"]["new_game"]:
                self.app.popup_control.create_New_Game()
            else:
                self.app.start_Saved_Game(
                    self.app.curr_userdata[self.app.curr_player][
                        "sa_games_data"
                    ][4]
                )

    def set_But_Names(self):
        self.ids.box_sg_1.ids.b_load_game.name = "b_gs_1_start"
        self.ids.box_sg_2.ids.b_load_game.name = "b_gs_2_start"
        self.ids.box_sg_3.ids.b_load_game.name = "b_gs_3_start"
        self.ids.box_sg_4.ids.b_load_game.name = "b_gs_4_start"
        self.ids.box_sg_5.ids.b_load_game.name = "b_gs_5_start"

    def logout_User(self):
        self.app.curr_player = ""
        self.app.login_state = 0
