from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from constants import *

from popups.popup_password.user_manager import load_user_data
from popups.popup_select_map.popup_select_map import PopupSelectMap

Builder.load_file(PATH_KV_STARTPAGE)


class StartPage(Screen):
    def __init__(self, app, **kwargs):
        super(StartPage, self).__init__(**kwargs)
        self.app = app
        self.state_game_selected = 0
        self.state_user_selected = 0
        self.ids.box_sg_1.ids.b_load_game.name = "b_gs_1_start"
        self.ids.box_sg_2.ids.b_load_game.name = "b_gs_2_start"
        self.ids.box_sg_3.ids.b_load_game.name = "b_gs_3_start"
        self.ids.box_sg_4.ids.b_load_game.name = "b_gs_4_start"
        self.ids.box_sg_5.ids.b_load_game.name = "b_gs_5_start"
        self.ids.box_sg_1.ids.b_load_game.bind(
            on_release=lambda dt: self.but_start_game_pressed(
                self.ids.box_sg_1.ids.b_load_game.name
            )
        )
        self.ids.box_sg_2.ids.b_load_game.bind(
            on_release=lambda dt: self.but_start_game_pressed(
                self.ids.box_sg_2.ids.b_load_game.name
            )
        )
        self.ids.box_sg_3.ids.b_load_game.bind(
            on_release=lambda dt: self.but_start_game_pressed(
                self.ids.box_sg_3.ids.b_load_game.name
            )
        )
        self.ids.box_sg_4.ids.b_load_game.bind(
            on_release=lambda dt: self.but_start_game_pressed(
                self.ids.box_sg_4.ids.b_load_game.name
            )
        )
        self.ids.box_sg_5.ids.b_load_game.bind(
            on_release=lambda dt: self.but_start_game_pressed(
                self.ids.box_sg_5.ids.b_load_game.name
            )
        )

    def update_start_page(self):
        self.set_But_State()
        self.update_Label_StartPage()

    def update_Label_StartPage(self):
        self.ids.box_tit.ids.lab_tit.text = self.app.lab_txt["start_page"]

        self.ids.lab_reg_users.text = f"{self.app.lab_txt['registered_users']}"
        self.ids.but_uname_1.text = self.app.saved_players[0]
        self.ids.but_uname_2.text = self.app.saved_players[1]
        self.ids.but_uname_3.text = self.app.saved_players[2]
        self.ids.but_uname_4.text = self.app.saved_players[3]
        self.ids.but_uname_5.text = self.app.saved_players[4]

        self.ids.box_u_info.ids.lab_tit_user_info.text = (
            f"{self.app.lab_txt['user_data']}: {self.app.curr_player}"
        )

        self.ids.box_u_info.ids.lab_r0_c0.text = self.app.lab_txt["creation_date"]
        self.ids.box_u_info.ids.lab_r1_c0.text = self.app.lab_txt["last_save"]
        self.ids.box_u_info.ids.lab_r2_c0.text = self.app.lab_txt["saved_games"]
        self.ids.box_u_info.ids.lab_r3_c0.text = self.app.lab_txt["played_games"]
        self.ids.box_u_info.ids.lab_r4_c0.text = self.app.lab_txt["last_game"]
        self.ids.box_u_info.ids.lab_r5_c0.text = self.app.lab_txt["tot_p_time"]

        if self.app.curr_player:
            self.ids.box_u_info.ids.lab_r0_c1.text = self.app.curr_p_data[
                "creation_date"
            ]
            self.ids.box_u_info.ids.lab_r1_c1.text = self.app.curr_p_data["last_save"]
            self.ids.box_u_info.ids.lab_r2_c1.text = str(
                self.app.curr_p_data["saved_games"]
            )
            self.ids.box_u_info.ids.lab_r3_c1.text = str(
                self.app.curr_p_data["played_games"]
            )
            self.ids.box_u_info.ids.lab_r4_c1.text = self.app.curr_p_data["last_game"]
            self.ids.box_u_info.ids.lab_r5_c1.text = self.app.curr_p_data["tot_p_time"]
        else:
            self.ids.box_u_info.ids.lab_r0_c1.text = ""
            self.ids.box_u_info.ids.lab_r1_c1.text = ""
            self.ids.box_u_info.ids.lab_r2_c1.text = ""
            self.ids.box_u_info.ids.lab_r3_c1.text = ""
            self.ids.box_u_info.ids.lab_r4_c1.text = ""
            self.ids.box_u_info.ids.lab_r5_c1.text = ""

        self.ids.but_new_user.text = self.app.lab_txt["new_player"]
        self.ids.but_new_game.text = self.app.lab_txt["new_game"]

        self.ids.lab_tit_game_saves.text = self.app.lab_txt["game_saves"]

        self.ids.box_sg_1.ids.img_map.source = (
            f'{DIR_IMAGES}{self.app.data_app["maps"]["sosnovka"]}'
        )
        self.ids.box_sg_1.ids.l_tit_game_name.text = self.app.lab_txt["game_name"]
        if self.app.curr_player:
            self.ids.box_sg_1.ids.l_game_name.text = (
                self.app.loaded_game_data_from_curr_player[self.app.curr_player][
                    "saved_games_data"
                ][0]["map_name"]
            )

        self.ids.box_sg_1.ids.b_load_game.text = self.app.f_let_upper(
            self.app.lab_txt["start"]
        )
        self.ids.box_sg_2.ids.b_load_game.text = self.app.f_let_upper(
            self.app.lab_txt["start"]
        )
        self.ids.box_sg_3.ids.b_load_game.text = self.app.f_let_upper(
            self.app.lab_txt["start"]
        )
        self.ids.box_sg_4.ids.b_load_game.text = self.app.f_let_upper(
            self.app.lab_txt["start"]
        )
        self.ids.box_sg_5.ids.b_load_game.text = self.app.f_let_upper(
            self.app.lab_txt["start"]
        )

        self.ids.box_sg_1.ids.b_del_game.text = self.app.f_let_upper(
            self.app.lab_txt["delete"]
        )
        self.ids.box_sg_2.ids.b_del_game.text = self.app.f_let_upper(
            self.app.lab_txt["delete"]
        )
        self.ids.box_sg_3.ids.b_del_game.text = self.app.f_let_upper(
            self.app.lab_txt["delete"]
        )
        self.ids.box_sg_4.ids.b_del_game.text = self.app.f_let_upper(
            self.app.lab_txt["delete"]
        )
        self.ids.box_sg_5.ids.b_del_game.text = self.app.f_let_upper(
            self.app.lab_txt["delete"]
        )

        self.ids.box_bottom.ids.but_settings.text = self.app.lab_txt["settings"]
        self.ids.box_bottom.ids.but_quit.text = self.app.f_let_upper(
            self.app.lab_txt["quit"]
        )

    def set_But_State(self):
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
        if not self.app.curr_player:
            self.ids.but_new_game.disabled = True
        else:
            self.ids.but_new_game.disabled = False

    def set_User(self, curr_uname):
        self.app.curr_u_name = curr_uname
        self.app.open_login_popup()
        self.app.login_state = 1
        self.app.saved_game_data_from_curr_player = load_user_data()

    def reg_user(self):
        self.app.popup_control.open_reg_user_popup()

        

    def but_start_game_pressed(self, name):
        if name == "b_gs_1_start":
            self.app.start_Saved_Game(
                self.app.saved_game_data_from_curr_player[self.app.curr_player][
                    "saved_games_data"
                ][0]
            )
        elif name == "b_gs_2_start":
            self.app.start_Saved_Game(
                self.app.saved_game_data_from_curr_player[self.app.curr_player][
                    "saved_games_data"
                ][1]
            )
        elif name == "b_gs_3_start":
            self.app.start_Saved_Game(
                self.app.saved_game_data_from_curr_player[self.app.curr_player][
                    "saved_games_data"
                ][2]
            )
        elif name == "b_gs_4_start":
            self.app.start_Saved_Game(
                self.app.saved_game_data_from_curr_player[self.app.curr_player][
                    "saved_games_data"
                ][3]
            )
        elif name == "b_gs_5_start":
            self.app.start_Saved_Game(
                self.app.saved_game_data_from_curr_player[self.app.curr_player][
                    "saved_games_data"
                ][4]
            )
