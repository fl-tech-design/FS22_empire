from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.lang import Builder


from constants import (
    DIR_POPUPS,
    DIR_SPLASH_SCR,
    PATH_DIR_IMG_CHO,
    DIR_MAPS,
    DIR_SIGNS,
)

from pages.loadingpage.loading_page import LoadingScreen

Builder.load_file(DIR_POPUPS + "popup_select_map/popup_sel_map.kv")


class PopupSelectMap(Popup):
    def __init__(self, scr_man, app, **kwargs):
        super(PopupSelectMap, self).__init__(**kwargs)
        self.app = app
        self.scr_man = scr_man
        self.txt_lab = self.app.lab_txt
        self.map_list = self.app.data_app["map_list"]
        self.map_index = 0
        self.ids.but_start_game.text = self.txt_lab["app"]["start_game"]
        self.ids.but_cancel.text = self.app.f_let_upper(self.txt_lab["verbs"]["cancel"])
        self.curr_map_data = self.app.data_app["maps"][self.map_list[self.map_index]]

        self.upd_pop_sel_map()

    def upd_pop_sel_map(self):
        self.curr_map_data = self.app.data_app["maps"][self.map_list[self.map_index]]
        self.upd_lab_txt()
        self.upd_img_sources()

        # set grid of side coordination
        self.ids.box_index_grid.clear_widgets()
        for i in range(len(self.app.data_app["map_list"])):
            if i == self.map_index:
                img_src = DIR_SIGNS + "img_sign_point_white.png"
            else:
                img_src = DIR_SIGNS + "img_sign_point_blue.png"
            img = Image(source=img_src)
            self.ids.box_index_grid.add_widget(img)

    def upd_lab_txt(self):
        self.ids.l_tit_map_info.text = (
            self.txt_lab["nouns"]["map_infos"].split()[1] + ":"
        )
        # Box Mapname with title and current name of map
        self.ids.row_inf_map_name.ids.l_tit_info_line.text = self.txt_lab["nouns"][
            "map_name"
        ].split()[1]
        self.ids.row_inf_map_name.ids.l_inf_line.text = self.curr_map_data["map_name"]

        # Box Location with title and current location
        self.ids.row_inf_map_location.ids.l_tit_info_line.text = self.txt_lab["nouns"][
            "location"
        ].split()[1]
        if self.curr_map_data["location"]:
            self.ids.row_inf_map_location.ids.l_inf_line.text = self.txt_lab["fs22"][
                self.curr_map_data["location"]
            ]
        else:
            self.ids.row_inf_map_location.ids.l_inf_line.text = ""
        # Box num_of_fields with title and current nums of fields of the map
        self.ids.row_inf_num_fields.ids.l_tit_info_line.text = self.txt_lab["app"][
            "num_of_fields"
        ].split()[1]
        if self.curr_map_data["num_of_fields"]:
            self.ids.row_inf_num_fields.ids.l_inf_line.text = self.curr_map_data[
                "num_of_fields"
            ]
        else:
            self.ids.row_inf_num_fields.ids.l_inf_line.text = ""

    def upd_img_sources(self):
        self.ids.img_map_cho.source = (
            PATH_DIR_IMG_CHO + "img_cho_" + self.map_list[self.map_index] + ".png"
        )
        self.ids.img_map.source = (
            DIR_MAPS + "img_map_" + self.map_list[self.map_index] + ".png"
        )

    def start_New_Game(self, *args):
        # Erstelle eine Instanz von LoadingScreen
        spl_scr_map = LoadingScreen(
            self.scr_man,
            self.app,
            self.txt_lab,
            DIR_SPLASH_SCR + "img_spl_" + self.map_list[self.map_index] + ".png",
            "page_main_game",
            0.005,
            0.001,
            name=self.map_list[self.map_index],
        )
        # Füge die Instanz von LoadingScreen zum ScreenManager hinzu
        self.scr_man.add_widget(spl_scr_map)
        self.dismiss()
        # Wechsle zum LoadingScreen
        self.app.scr_man.current = self.map_list[self.map_index]

    def decr_map_index(self):
        if self.map_index > 0:
            self.map_index -= 1
        self.upd_pop_sel_map()

    def incr_map_index(self):
        if self.map_index < len(self.app.data_app["map_list"]) - 1:
            self.map_index += 1
        self.upd_pop_sel_map()
