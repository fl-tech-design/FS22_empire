# loading_page.py

from kivy.uix.screenmanager import Screen, SlideTransition, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
import time


class LoadingScreen(Screen):
    def __init__(
        self,
        scr_manager,
        app,
        lab_txt,
        spl_scr,
        new_page,
        prog_bar_y=0.2,
        stat_lab_y=0.15,
        **kwargs,
    ):
        super(LoadingScreen, self).__init__(**kwargs)
        self.app = app
        self.scr_man = scr_manager  # Referenz auf den ScreenManager
        self.txt_lab = lab_txt
        self.new_page = new_page
        layout = FloatLayout()

        # Hintergrundbild
        self.background = Image(source=spl_scr, fit_mode="fill")
        layout.add_widget(self.background)

        # Fortschrittsanzeige
        self.progress_bar = ProgressBar(
            max=100, size_hint=(1, 0.25), pos_hint={"x": 0, "y": prog_bar_y}
        )
        layout.add_widget(self.progress_bar)

        # Statuslabel
        self.status_label = Label(
            size_hint=(0.8, 0.15),
            text=self.app.f_let_upper(self.txt_lab["status"]["loading"] + "..."),
            pos_hint={"x": 0.1, "y": stat_lab_y},
        )
        layout.add_widget(self.status_label)

        self.add_widget(layout)

        # Starte den Ladevorgang
        Clock.schedule_once(self.start_loading, 1)

    def start_loading(self, dt):
        Clock.schedule_interval(self.load_data, 0.01)
        self.loading_progress = 0

    def load_data(self, dt):
        # Simuliere das Laden von Daten
        time.sleep(0.1)
        self.loading_progress += 10
        self.progress_bar.value = self.loading_progress
        self.status_label.text = self.app.f_let_upper(
            f'{self.txt_lab["status"]["loading"]}...  {self.loading_progress}%'
        )
        self.status_label.font_size = "42sp"

        if self.loading_progress >= 100:
            Clock.unschedule(self.load_data)
            self.status_label.text = f'{self.txt_lab["status"]["loading_complete"]}!'
            Clock.schedule_once(self.go_to_main_screen, 1)

    def go_to_main_screen(self, dt):
        self.scr_man.transition = NoTransition()  # Set NoTransition
        self.scr_man.current = self.new_page
        self.scr_man.transition = SlideTransition()  # Set NoTransition
