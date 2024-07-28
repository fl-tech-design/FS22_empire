from kivy.uix.popup import Popup

from kivy.lang import Builder

from constants import DIR_POPUPS

Builder.load_file(DIR_POPUPS + "pop_info/pop_info.kv")


class Pop_Info(Popup):
    def __init__(self, app, info_msg: str, **kwargs):
        super(Pop_Info, self).__init__(**kwargs)
        self.app = app
        self.title = f'{self.app.lab_txt["app"]["information"]}'
        self.ids.l_descr_help.text = info_msg
        self.ids.but_close_popup.text = self.app.f_let_upper(self.app.lab_txt["verbs"]["close"])
    
    def close_Popup(self):
        self.dismiss()