from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

from control_data import DataControl
from constants import *

from pages.loadingpage.loading_page import LoadingScreen
from pages.page_start.startpage import StartPage
from pages.page_settings.settingpage import SettingPage
from pages.page_buy_item.pagebuyitem import PageBuyItem
from pages.maplayoutpage.maplayoutpage import PageMapLayout
from pages.page_main_game.pagemaingame import PageMainGame

from popups.popup_help.popup_help import PopupHelp
from popups.popup_new_lkw import Popup_New_Lkw
from popups.popup_password.popup_log_user import LoginPopup
from popups.popup_password.popup_reg_user import RegisterPopup
from popups.popup_select_map.popup_sel_map import PopupSelectMap
from popups.popup_sel_comp import CompanySelectionPopup
from popups.popup_password.user_manager import load_user_data


Builder.load_file(PATH_KV_COLORS)
Builder.load_file(PATH_KV_BOXES)
Builder.load_file(PATH_KV_COMPONENTS)
Builder.load_file(PATH_KV_WIDGETS)


class PopupControl:
    def __init__(self, scr_man, **kwargs) -> None:
        """
        Initialisierung der Variabeln.
        """
        self.login_state = 0

    def open_new_lkw_popup(self) -> None:
        popup = Popup_New_Lkw(app.lab_txt)
        popup.open()

    def open_new_tractor_popup(self) -> None:
        popup = Popup_New_Lkw(app.lab_txt)
        popup.open()

    def open_reg_user_popup(self) -> None:
        popup = RegisterPopup(app)
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
        # Klassenw werden initialisiert
        self.control_data = DataControl(app)
        self.scr_man = ScreenManager()
        self.popup_control = PopupControl(self.scr_man)

        # Daten werden geladen
        self.data_app = self.control_data.return_Data_App()
        self.curr_language = self.data_app["curr_language"]
        self.lab_txt = self.control_data.return_Lab_Txt(self.curr_language)
        self.len_list_map = len(self.data_app["map_list"])

        # App Grundeinstellungen werden gesetzt
        Window.maximize()
        self.title = self.data_app["app_name"]
        self.app_version = VERSION_NR

        # Uservariabel werden erstellt
        self.curr_u_name = ""
        self.curr_player = ""
        self.curr_u_data = {}
        self.curr_userdata = load_user_data()

        # Mapvariabeln werden erstellt
        self.map_list = self.data_app["map_list"]
        print(self.map_list)
        map_data = self.control_data.return_Map_Data(self.map_list)
        print("map_data:\n", map_data)
        self.curr_map_name = ""
        self.curr_map = ""

        # Spielvariabeln werden definiert. diese Variabeln werden für den Spielstand eines Spiels gebraucht, also wiederverwendbar
        # für andere Spielstände
        self.curr_g_data = {}


        # allgemeine gamevariabeln.
        self.saved_players = self.data_app["saved_players"]
        self.saved_players_index = 0



        # Definition LoadingScreen Start App
        self.spl_scr_start = LoadingScreen(
            self.scr_man,
            app,
            self.lab_txt,
            SPL_SCREEN_START_APP,
            "page_start",
            name="spl_scr_start",
        )
        self.scr_man.add_widget(self.spl_scr_start)

        # Definition Page One. The Startscreen
        self.page_start = StartPage(app, self.scr_man)
        screen = Screen(name="page_start")
        screen.add_widget(self.page_start)
        self.scr_man.add_widget(screen)

        # Definition Page Two. Settingscreen
        self.page_settings = SettingPage(app)
        screen = Screen(name="page_settings")
        screen.add_widget(self.page_settings)
        self.scr_man.add_widget(screen)

        # Definition Page Three. My factories screen.
        self.page_map_layout = PageMapLayout(app)
        screen = Screen(name="page_map_layout")
        screen.add_widget(self.page_map_layout)
        self.scr_man.add_widget(screen)

        # Definition Page Four. The "buy new Truck screen"
        self.page_buy_item = PageBuyItem(app)
        screen = Screen(name="page_buy_item")
        screen.add_widget(self.page_buy_item)
        self.scr_man.add_widget(screen)

        # Definition Page Five. The Mainscreen of the Game
        self.page_main_game = PageMainGame(app, self.scr_man)
        screen = Screen(name="page_main_game")
        screen.add_widget(self.page_main_game)
        self.scr_man.add_widget(screen)


        # Clock loop
        Clock.schedule_interval(self.update_app_loop, 0.2)
        Clock.max_iteration = 22  # Standardwert ist 20
        # start app
        return self.scr_man

    def update_app_loop(self, *args):
        if self.scr_man.current == "page_start":
            self.page_start.update_page_start()
        elif self.scr_man.current == "page_settings":
            self.page_settings.update_page_settings()
        elif self.scr_man.current == "page_4":
            self.page_buy_item.update_labels()
        elif self.scr_man.current == "page_5":
            self.page5.update_Page_5()

    def change_Screen(self, new_transition: str, new_scr_name: str) -> None:
        """
        Changes the current screen displayed by the application.

        :param new_transition: The transition direction for the screen change.
        :type new_transition: str
        :param new_scr_name: The name of the new screen to display.
        :type new_scr_name: str
        :return: None.
        :rtype: None
        """
        self.scr_man.transition.direction = new_transition
        self.scr_man.current = new_scr_name

    def on_time_set(self, hours, minutes):
        # Hier kannst du die Zeit setzen oder andere Aktionen ausführen
        self.status = True  # Beispiel: Zeitstatus auf True setzen

    def reload_app_data(self):
        self.data_app = self.control_data.return_Data_App()
        self.curr_language = self.data_app["curr_language"]
        self.lab_txt = self.control_data.return_Lab_Txt(self.curr_language)
        self.saved_players = self.data_app["saved_players"]

    def open_login_popup(self):
        self.login_popup = LoginPopup(self.on_login_success, app)
        self.login_popup.open()

    def on_login_success(self, username):
        self.login_popup.dismiss()
        if self.login_state:
            self.curr_player = username
            self.curr_u_data = app.control_data.get_curr_player_data(username)
        self.control_data.set_Data_App("curr_player_name", username)
        self.control_data.set_Last_Login(username)

    def start_Saved_Game(self, game_data: dict):
        self.curr_g_data = game_data

    def f_let_upper(self, str_small):
        txt = str_small
        new_txt = txt[0].upper() + txt[1:]
        return new_txt


if __name__ == "__main__":
    app = MainApp()
    app.run()
