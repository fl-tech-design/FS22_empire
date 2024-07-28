from kivy.uix.popup import Popup

from kivy.lang import Builder

from constants import DIR_POPUPS

Builder.load_file(DIR_POPUPS + "pop_set_clock/pop_set_clock.kv")


class Pop_Set_Clock(Popup):
    def __init__(self, app, **kwargs):
        super(Pop_Set_Clock, self).__init__(**kwargs)
        self.app = app
        self.title = f'{self.app.lab_txt["app"]["set_clock"]}'
        self.ids.l_descr_set_time.text = f'{self.app.lab_txt["descr"]["descr_set_clock"]}'
        self.ids.but_close_popup.text = self.app.f_let_upper(self.app.lab_txt["verbs"]["close"])
    
    def close_Popup(self):
        self.dismiss()