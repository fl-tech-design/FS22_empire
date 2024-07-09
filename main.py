from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

from control_data import DataControl

from pages.mappage.mappage import MapLayout

from loading_screen import LoadingScreen

from popups.popup_new_lkw import Popup_New_Lkw
from popups.popup_sel_comp import CompanySelectionPopup

from popups.popup_password.popup_log_user import LoginPopup
from popups.popup_password.popup_reg_user import RegisterPopup
from popups.popup_password.user_manager import load_user_data

from constants import *

from pages.startpage.startpage import StartPage
from pages.settingpage.settingpage import SettingPage
from pages.buyitempage.buyitempage import BuyItemPage


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

    def open_time_set_popup(self, instance):
        if not self.status:
            self.popup.open()


class PageMapLayout(Screen):
    def __init__(self, **kwargs):
        super(PageMapLayout, self).__init__(**kwargs)
        self.map_layout = MapLayout(app.lab_txt, app)
        self.add_widget(self.map_layout)


class Page5(Screen):
    def __init__(self, **kwargs):
        super(Page5, self).__init__(**kwargs)
        self.data_curr_game = {}

    def update_Page_5(self):
        self.ids.box_tit.ids.lab_tit.text = self.first_letter_upper(
            app.lab_txt["in_the_office"]
        )


class MainApp(App):
    def build(self):
        global app
        app = self

        self.control_data = DataControl(app)
        self.popup_control = PopupControl()

        self.data_app = self.control_data.read_data_app()
        self.curr_language = self.data_app["curr_language"]
        self.lab_txt = self.control_data.read_data_txt(self.curr_language)
        self.data_trucks = self.control_data.load_trucks_from_json()

        # App Grundeinstellungen werden gesetzt
        Window.maximize()
        self.title = self.data_app["app_name"]
        self.app_version = VERSION_NR

        # Spielvariabeln werden erstellt
        self.curr_u_name = ""
        self.curr_player = ""
        self.curr_map = ""

        self.curr_data_game = {}

        self.loaded_game_data_from_curr_player = load_user_data()

        self.saved_players = self.data_app["saved_players"]
        self.saved_players_index = 0

        self.map_select_state = 0

        # Klasse ScreenManager wird initialisiert.
        self.scr_man = ScreenManager()

        # Definition LoadingScreen
        self.loading_screen = LoadingScreen(
            scr_manager=self.scr_man, lab_txt=self.lab_txt, name="loading_screen"
        )
        self.scr_man.add_widget(self.loading_screen)

        # Definition Page One. The Startscreen
        self.start_page = StartPage(app)
        screen = Screen(name="start_page")
        screen.add_widget(self.start_page)
        self.scr_man.add_widget(screen)

        # Definition Page Two. Settingscreen
        self.setting_page = SettingPage(app)
        screen = Screen(name="setting_page")
        screen.add_widget(self.setting_page)
        self.scr_man.add_widget(screen)

        # Definition Page Three. My factories screen.
        self.page_map_layout = PageMapLayout()
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

        self.clock_set_stat = False
        self.time_scale = 1
        self.time_game_h = 0
        self.time_game_m = 0
        self.loop_counter = 0
        Clock.schedule_interval(lambda dt: self.update_app_loop(), 0.2)
        Clock.max_iteration = 22  # Standardwert ist 20
        return self.scr_man

    def update_app_loop(self):
        self.loop_counter += 1
        if self.clock_set_stat:
            if self.loop_counter % 300 / self.time_scale == 1:
                self.time_game_m += 1
                if self.time_game_m >= 59:
                    self.time_game_m = 0
                    self.time_game_h += 1
                    if self.time_game_h > 23:
                        self.time_game_h = 0

        if self.scr_man.current == "start_page":
            self.start_page.update_start_page()
        elif self.scr_man.current == "setting_page":
            self.setting_page.update_setting_page()
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
        print(f"Zeit eingestellt: {hours} Stunden, {minutes} Minuten")
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
            self.curr_p_data = app.control_data.get_curr_player_data(username)

    def start_new_game(self, instance):
        # Code to start a new game
        pass

    def start_Saved_Game(self, game_data: dict):
        print("start_Saved_Game() called")
        self.curr_data_game = game_data
        print(game_data)

    def first_letter_upper(self, str_small):
        txt = str_small
        new_txt = txt[0].upper() + txt[1:]
        return new_txt



if __name__ == "__main__":
    app = MainApp()
    app.run()
