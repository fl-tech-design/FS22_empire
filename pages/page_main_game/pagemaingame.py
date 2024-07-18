# pagemaingame.py

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from constants import PATH_KV_PAGEMAINGAME


Builder.load_file(PATH_KV_PAGEMAINGAME)


class StartPageUpdater:
    def __init__(self, app, ids):
        self.app = app
        self.ids = ids

    def update(self):
        self.upd_box_title()
    
    def upd_box_title(self):
        self.ids.box_tit_maingame.ids.lab_tit.text = self.app.f_let_upper(self.app.lab_txt["app"]["main_menu"])
        self.ids.box_bot_maingame.ids.but_1.text = self.app.f_let_upper(self.app.lab_txt["app"]["logout"])
        self.ids.box_bot_maingame.ids.but_2.text = self.app.f_let_upper(self.app.lab_txt["app"]["quit"])


class PageMainGame(Screen):
    def __init__(self, app, scr_man, **kwargs):
        super(PageMainGame, self).__init__(**kwargs)
        self.app = app
        self.scr_man = scr_man
        # GameTime vars
        self.clock_set_stat = False
        self.time_scale = 1
        self.time_game_h = 0
        self.time_game_m = 0
        self.loop_counter = 0
        self.upd_Page_Main_Game()

    def upd_Page_Main_Game(self):
        updater = StartPageUpdater(self.app, self.ids)
        updater.update()
        if self.clock_set_stat:
            if self.loop_counter % 300 / self.time_scale == 1:
                self.time_game_m += 1
                if self.time_game_m >= 59:
                    self.time_game_m = 0
                    self.time_game_h += 1
                    if self.time_game_h > 23:
                        self.time_game_h = 0
