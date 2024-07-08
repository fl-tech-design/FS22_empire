from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import NumericProperty
from constants import *

Builder.load_file(PATH_KV_SETTINGPAGE)


class SettingPage(Screen):
    def __init__(self, app, **kwargs):
        super(SettingPage, self).__init__(**kwargs)
        self.app = app
        self.admin_state = 0

    def update_setting_page(self):
        self.set_Admin_But_State()
        self.update_labels()

    def set_Admin_But_State(self):
        if self.admin_state:
            self.ids.but_new_lkw.disabled = False
            self.ids.but_new_tractor.disabled = False
        else:
            self.ids.but_new_lkw.disabled = True
            self.ids.but_new_tractor.disabled = True

    def update_labels(self):
        self.ids.box_tit.ids.lab_tit.text = self.app.lab_txt["settings"]
        self.ids.lab_tit_admin_settings.text = self.app.lab_txt["admin_settings"]
        self.ids.lab_tit_admin_sett_descr.text = self.app.lab_txt["descr_admin_sett"]

        self.ids.lab_tit_sett_game.text = self.app.lab_txt["game_settings"]
        self.ids.lab_time_scale.text = self.app.lab_txt["time_scale"]
        self.ids.lab_d_p_month.text = self.app.lab_txt["days_per_month"]
        self.ids.lab_tit_sett_general.text = self.app.lab_txt["general_settings"]

        if self.admin_state:
            self.ids.but_admin.text = self.app.lab_txt["quit"]
        else:
            self.ids.but_admin.text = self.app.lab_txt["admin"]

        self.ids.but_new_lkw.text = self.app.lab_txt["new_truck"]
        self.ids.but_new_tractor.text = self.app.lab_txt["new_tractor"]

        self.ids.box_bottom.ids.but_settings.text = self.app.lab_txt["back"]
        self.ids.box_bottom.ids.but_quit.text = self.app.lab_txt["quit"]

    def adminbutton_pressed(self):
        if self.admin_state:
            self.admin_state = 0
        else:
            self.admin_state = 1
