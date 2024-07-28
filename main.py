from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock

from control_data import DataControl
from constants import *

from pages.loadingpage.loading_page import LoadingScreen
from pages.page_start.startpage import StartPage
from pages.page_settings.settingpage import SettingPage
from pages.page_main_game.pagemaingame import PageMainGame
from pages.page_game_map.page_game_map import PageGameMap

from popups.popup_help.popup_help import PopupHelp
from popups.popup_new_lkw import Popup_New_Lkw
from popups.popup_password.pop_log_user import Pop_Login
from popups.popup_select_map.popup_sel_map import PopupSelectMap
from popups.popup_sel_comp import CompanySelectionPopup
from popups.popup_password.user_manager import PwManager

Builder.load_file(PATH_KV_COLORS)
Builder.load_file(PATH_KV_BOXES)
Builder.load_file(PATH_KV_COMPONENTS)
Builder.load_file(PATH_KV_WIDGETS)


class PopupControl:
    def __init__(self, scr_man, **kwargs) -> None:
        self.login_state = 0

    def open_new_lkw_popup(self) -> None:
        popup = Popup_New_Lkw(app.lab_txt)
        popup.open()

    def open_new_tractor_popup(self) -> None:
        popup = Popup_New_Lkw(app.lab_txt)
        popup.open()

    def open_sel_comp_popup(self):
        popup = CompanySelectionPopup(app.lab_txt)
        popup.open()

    def create_New_Game(self, scr_man, *args):
        popup = PopupSelectMap(scr_man, app)
        popup.open()

    def open_Help_popup(self, page_name, *args):
        popup = PopupHelp(app, page_name)
        popup.open()


class MainApp(App):
    def build(self):
        global app
        app = self
        self.control_data = DataControl(app)
        self.scr_man = ScreenManager()
        self.popup_control = PopupControl(self.scr_man)
        self.pw_man = PwManager(app)

        self.data_app = self.control_data.return_Data_App()
        self.curr_language = self.data_app["curr_language"]
        self.lab_txt = self.control_data.return_Lab_Txt(self.curr_language)

        self.title = self.data_app["app_name"]
        self.app_version = VERSION_NR

        self.user_name = ""
        self.user_data = {}
        self.user_list = self.data_app["user_list"]
        self.user_list_index = 0
        self.login_state = 0

        self.map_name = ""
        self.map_id = ""
        self.map_list = self.data_app["map_list"]
        self.map_list_len = len(self.data_app["map_list"])
        self.map_data = {}

        self.spl_scr_start = LoadingScreen(
            self.scr_man,
            app,
            self.lab_txt,
            SPL_SCREEN_START_APP,
            "page_start",
            name="spl_scr_start",
        )
        self.scr_man.add_widget(self.spl_scr_start)

        self.page_start = StartPage(app, self.scr_man)
        screen = Screen(name="page_start")
        screen.add_widget(self.page_start)
        self.scr_man.add_widget(screen)

        self.page_settings = SettingPage(app)
        screen = Screen(name="page_settings")
        screen.add_widget(self.page_settings)
        self.scr_man.add_widget(screen)

        self.page_main_game = PageMainGame(app, self.scr_man)
        screen = Screen(name="page_main_game")
        screen.add_widget(self.page_main_game)
        self.scr_man.add_widget(screen)

        self.page_game_map = PageGameMap(app, self.scr_man)
        screen = Screen(name="page_game_map")
        screen.add_widget(self.page_game_map)
        self.scr_man.add_widget(screen)

        Clock.schedule_interval(self.update_app_loop, 0.3)
        Clock.max_iteration = 22
        return self.scr_man

    def update_app_loop(self, *args):
        if self.scr_man.current == "page_start":
            self.page_start.update_page_start()
        elif self.scr_man.current == "page_settings":
            self.page_settings.update_page_settings()
        elif self.scr_man.current == "page_main_game":
            self.page_main_game.upd_Page_Main_Game()
        elif self.scr_man.current == "page_game_map":
            self.page_game_map.upd_Page_Game_Map()

    def change_Screen(self, new_transition: str, new_scr_name: str) -> None:
        self.scr_man.transition.direction = new_transition
        self.scr_man.current = new_scr_name

    def reload_app_data(self):
        self.data_app = self.control_data.return_Data_App()
        self.curr_language = self.data_app["curr_language"]
        self.lab_txt = self.control_data.return_Lab_Txt(self.curr_language)
        self.user_list = self.data_app["user_list"]

    def f_let_upper(self, str_small):
        txt = str_small
        new_txt = txt[0].upper() + txt[1:]
        return new_txt


if __name__ == "__main__":
    app = MainApp()
    app.run()
