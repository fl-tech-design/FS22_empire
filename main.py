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
from pages.buyitempage.buyitempage import BuyItemPage
from pages.maplayoutpage.maplayoutpage import PageMapLayout

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
    def __init__(self, **kwargs) -> None:
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

    def create_New_Game(self, *args):
        popup = PopupSelectMap(app)
        popup.open()

    def open_Help_popup(self, page_name, *args):
        popup = PopupHelp(app, page_name)
        popup.open()
            
        
class Page5(Screen):
    def __init__(self, **kwargs):
        super(Page5, self).__init__(**kwargs)
        self.data_curr_game = {}

    def update_Page_5(self):
        self.ids.box_tit.ids.lab_tit.text = self.f_let_upper(
            app.lab_txt["in_the_office"]
        )


class MainApp(App):
    def build(self):
        global app
        app = self
        # Klassenw werden initialisiert
        self.control_data = DataControl(app)
        self.popup_control = PopupControl()

        # Daten werden geladen
        self.data_app = self.control_data.read_data_app()
        self.curr_language = self.data_app["curr_language"]
        self.lab_txt = self.control_data.read_data_txt(self.curr_language)
        self.data_trucks = self.control_data.load_trucks_from_json()
        self.len_list_map = len(self.data_app["map_list"])

        # App Grundeinstellungen werden gesetzt
        Window.maximize()
        self.title = self.data_app["app_name"]
        self.app_version = VERSION_NR

        # Spielvariabeln werden erstellt
        self.curr_u_name = ""
        self.curr_player = ""
        self.curr_u_data = {}
        self.curr_map = ""

        self.curr_g_data = {}

        self.loaded_user_data_from_curr_player = load_user_data()

        self.saved_players = self.data_app["saved_players"]
        self.saved_players_index = 0

        self.map_select_state = 0

        # Klasse ScreenManager wird initialisiert.
        self.scr_man = ScreenManager()

        # Definition LoadingScreen Start App
        self.loading_screen = LoadingScreen(
            self.scr_man, self.lab_txt, SPL_SCREEN_START_APP, name="loading_screen"
        )
        self.scr_man.add_widget(self.loading_screen)

        # Definition Page One. The Startscreen
        self.page_start = StartPage(app)
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
        self.buy_item_page = BuyItemPage(app)
        screen = Screen(name="buy_item_page")
        screen.add_widget(self.buy_item_page)
        self.scr_man.add_widget(screen)

        # Definition Page Five. The Mainscreen of the Game
        self.page5 = Page5()
        screen = Screen(name="page_5")
        screen.add_widget(self.page5)
        self.scr_man.add_widget(screen)

        # GameTime vars
        self.clock_set_stat = False
        self.time_scale = 1
        self.time_game_h = 0
        self.time_game_m = 0
        self.loop_counter = 0
        
        # Clock loop 
        Clock.schedule_interval(self.update_app_loop, 0.2)
        Clock.max_iteration = 22  # Standardwert ist 20

        # start app
        return self.scr_man

    def update_app_loop(self, *args):
        self.loop_counter += 1
        if self.clock_set_stat:
            if self.loop_counter % 300 / self.time_scale == 1:
                self.time_game_m += 1
                if self.time_game_m >= 59:
                    self.time_game_m = 0
                    self.time_game_h += 1
                    if self.time_game_h > 23:
                        self.time_game_h = 0

        if self.scr_man.current == "page_start":
            self.page_start.update_page_start()
        elif self.scr_man.current == "page_settings":
            self.page_settings.update_page_settings()
        elif self.scr_man.current == "page_4":
            self.buy_item_page.update_labels()
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
        self.data_app = self.control_data.read_data_app()
        self.curr_language = self.data_app["curr_language"]
        self.lab_txt = self.control_data.read_data_txt(self.curr_language)
        self.data_trucks = self.control_data.load_trucks_from_json()
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
        self.control_data.set_Last_Login(username);

    def start_Saved_Game(self, game_data: dict):
        self.curr_g_data = game_data

    def f_let_upper(self, str_small):
        txt = str_small
        new_txt = txt[0].upper() + txt[1:]
        return new_txt


if __name__ == "__main__":
    app = MainApp()
    app.run()
