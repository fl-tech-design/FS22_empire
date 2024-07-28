from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from constants import PATH_KV_PAGEMAINGAME, DIR_MAPS
from popups.pop_set_clock.pop_set_clock import Pop_Set_Clock

Builder.load_file(PATH_KV_PAGEMAINGAME)


class MainPageUpdater:
    def __init__(self, app, ids):
        self.app = app
        self.ids = ids
        self.ids.box_bot_maingame.ids.but_1.bind(on_release=lambda dt: self.app.change_Screen("left", "page_start"))
        self.map_path = f"{DIR_MAPS}{list(self.app.map_data.keys())[0]}/map_{list(self.app.map_data.keys())[0]}.png"
        self.ids.box_map.ids.img_game_map.source = self.map_path

    def update(self):
        self.upd_box_title()
        self.upd_box_map()
        self.upd_box_bott()

    def upd_box_title(self):
        self.ids.box_tit_maingame.ids.lab_tit.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["main_menu"]
        )

    def upd_box_map(self):
        self.ids.box_map.ids.b_open_map.text = self.app.lab_txt["app"]["open_map"]

    def upd_box_bott(self):
        self.ids.box_bot_maingame.ids.but_1.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["logout"]
        )
        self.ids.box_bot_maingame.ids.but_2.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["quit"]
        )


class PageMainGame(Screen):
    def __init__(self, app, scr_man, **kwargs):
        super(PageMainGame, self).__init__(**kwargs)
        self.app = app
        self.scr_man = scr_man
        self.ids.box_map.ids.b_open_map.bind(on_release=self.open_Map_Page)

    def upd_Page_Main_Game(self):
        updater = MainPageUpdater(self.app, self.ids)
        updater.update()

    def set_Game_Time(self):
        pop = Pop_Set_Clock(self.app)
        pop.open()

    def open_Map_Page(self, *args):
        self.app.change_Screen("right", "page_game_map")
