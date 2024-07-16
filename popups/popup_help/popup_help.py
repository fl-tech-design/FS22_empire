from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.lang import Builder

from constants import DIR_POPUPS, DIR_IMAGES, PATH_DIR_IMG_CHO

Builder.load_file(DIR_POPUPS + "popup_help/popup_help.kv")


class PopupHelp(Popup):
    def __init__(self, app, curr_page_name, **kwargs):
        super(PopupHelp, self).__init__(**kwargs)
        self.app = app
        self.txt_lab = self.app.lab_txt
        self.title = f'Hilfe: {self.app.lab_txt["app"][curr_page_name]}'
        self.ids.l_descr_help.text = self.app.lab_txt["descr"][f'descr_help_{curr_page_name}']
        self.ids.but_close_popup.text = self.app.f_let_upper(self.app.lab_txt["verbs"]["close"])
    
    def close_Popup(self):
        self.dismiss()