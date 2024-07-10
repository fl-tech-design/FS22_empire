from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder

from constants import DIR_POPUPS, DIR_IMAGES

Builder.load_file(DIR_POPUPS + "popup_select_map/popup_select_map.kv")


class PopupSelectMap(Popup):
    def __init__(self, app, **kwargs):
        super(PopupSelectMap, self).__init__(**kwargs)
        self.app = app
        self.txt_lab = self.app.lab_txt
        self.map_index = 0
        self.update_map_image()
        
    def update_map_image(self):
        self.ids.img_map.source = DIR_IMAGES + self.app.data_app['map_list'][self.map_index]
        
    def decr_map_index(self):
        if self.map_index > 0:
            self.map_index -= 1
        self.update_map_image()
    
    def incr_map_index(self):
        print(len(self.app.data_app['map_list']) -1)
        if self.map_index < len(self.app.data_app['map_list']) - 1:
            self.map_index += 1
        self.update_map_image()
        