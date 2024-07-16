# loading_screen.py

from kivy.uix.screenmanager import Screen, SlideTransition, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
import time



class LoadingScreen(Screen):
    def __init__(self, scr_manager, lab_txt, spl_scr, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        self.scr_man = scr_manager  # Referenz auf den ScreenManager
        self.txt_lab = lab_txt
        layout = FloatLayout()

        # Hintergrundbild
        self.background = Image(source=spl_scr, fit_mode="fill")
        layout.add_widget(self.background)

        # Fortschrittsanzeige
        self.progress_bar = ProgressBar(
            max=100, size_hint=(0.8, 0.15), pos_hint={"x": 0.1, "y": 0.2}
        )
        layout.add_widget(self.progress_bar)

        # Statuslabel
        self.status_label = Label(
            text=self.txt_lab["status"]["loading"] + "...",
            size_hint=(0.8, 0.1),
            pos_hint={"x": 0.1, "y": 0.18},
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
        time.sleep(0.05)
        self.loading_progress += 10
        self.progress_bar.value = self.loading_progress
        self.status_label.text = (
            f'{self.txt_lab["status"]["loading"]}...  {self.loading_progress}%'
        )

        if self.loading_progress >= 100:
            Clock.unschedule(self.load_data)
            self.status_label.text = f'{self.txt_lab["status"]["loading_complete"]}!'
            Clock.schedule_once(self.go_to_main_screen, 1)

    def go_to_main_screen(self, dt):
        self.scr_man.transition = NoTransition()  # Set NoTransition
        self.scr_man.current = "page_start"
        self.scr_man.transition = SlideTransition()  # Set NoTransition
