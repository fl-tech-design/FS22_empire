from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from constants import PATH_KV_PAGEGAMEMAP, DIR_MAPS, DIR_SIGNS

Builder.load_file(PATH_KV_PAGEGAMEMAP)


class PageGameMapUpdater(Screen):
    def __init__(self, app, ids, set_but_state, **kwargs):
        super(PageGameMapUpdater, self).__init__(**kwargs)
        self.app = app
        self.ids = ids
        self.s_but_stat = set_but_state
        self.map_data = self.app.map_data[list(self.app.map_data.keys())[0]]
        self.map_path = f"{DIR_MAPS}{list(self.app.map_data.keys())[0]}/map_{list(self.app.map_data.keys())[0]}.png"
        self.ids.game_map.ids.i_map.source = self.map_path

        self.update()

    def add_buttons(self):
        if not self.s_but_stat:
            for entry in self.map_data["already_installed"]:
                pos = entry["pos"]
                icon_n_path = f"{DIR_SIGNS}{entry['icon_n']}"
                icon_d_path = f"{DIR_SIGNS}{entry['icon_d']}"
                btn = Button(
                    #text=entry["name"],
                    size_hint=(None, None),
                    size=(30, 30),
                    pos=pos,
                    background_normal=icon_n_path,
                    background_down=icon_d_path,
                )
                self.ids.game_map.add_widget(btn)
        self.s_but_stat = True

    def update(self):
        self.upd_box_title()
        self.upd_box_bott()
        self.add_buttons()

    def upd_box_title(self):
        self.ids.box_tit_game_map.ids.lab_tit.text = self.app.f_let_upper(
            self.map_data["map_name"]
        )

    def upd_box_bott(self):
        self.ids.box_bot_game_map.ids.but_1.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["back"]
        )
        self.ids.box_bot_game_map.ids.but_2.text = self.app.f_let_upper(
            self.app.lab_txt["app"]["quit"]
        )


class PageGameMap(Screen):
    def __init__(self, app, scr_man, **kwargs):
        super(PageGameMap, self).__init__(**kwargs)
        self.app = app
        self.scr_man = scr_man
        self.but_set_state = False
        self.ids.box_bot_game_map.ids.but_1.bind(
            on_release=lambda dt: self.app.change_Screen("left", "page_main_game")
        )

    def upd_Page_Game_Map(self):
        updater = PageGameMapUpdater(self.app, self.ids, self.but_set_state)
        updater.update()
