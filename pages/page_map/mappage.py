from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import json

from constants import *


class PageMap(FloatLayout):
    arrow_image = None
    placing_arrow = False
    arrow_id_counter = 0
    popup_open = False

    def __init__(self, lab_txt, app, **kwargs):
        super(PageMap, self).__init__(**kwargs)

        self.txt_lab = lab_txt
        self.app = app

        self.arrow_buttons = {}
        self.current_arrow_id = None

        self.current_g_name = ""

        # Hintergrundbild hinzufügen
        self.background = Image(
            source = "",
            fit_mode="fill",
        )
        self.add_widget(self.background)

        # Werkzeugleiste hinzufügen
        toolbar = BoxLayout(size_hint=(1, None), height=50, padding=10, spacing=10)
        with toolbar.canvas.before:
            from kivy.graphics import Color, Rectangle

            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=toolbar.size, pos=toolbar.pos)
        toolbar.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(toolbar)

        # Drei verschiedene Pfeile hinzufügen
        self.arrow_images = [
            "app_pics/img_signs/arrow1.png",
            "app_pics/img_signs/arrow2.png",
            "app_pics/img_signs/arrow3.png",
            "app_pics/img_signs/arrow4.png",
        ]

        for i in range(len(self.arrow_images)):
            arrow_button = Button(
                background_normal=self.arrow_images[i],
                size_hint=(None, None),
                size=(40, 40),
            )
            arrow_button.bind(on_press=self.start_placing_arrow)
            toolbar.add_widget(arrow_button)

        # Zurück-Button hinzufügen
        back_button = Button(text="Zurück", size_hint=(None, None), size=(100, 40))
        back_button.bind(on_release=self.go_back)
        toolbar.add_widget(back_button)

        # Laden der gespeicherten Buttons
        self.load_arrows()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def start_placing_arrow(self, instance):
        if not self.placing_arrow:
            self.placing_arrow = True
            self.arrow_image = Image(
                source=instance.background_normal,
                size_hint=(None, None),
                size=(40, 40),
                fit_mode="scale-down",
            )
            self.current_arrow_id = None
            self.add_widget(self.arrow_image)
            Clock.schedule_interval(self.update_arrow_position, 0)
            self.bind(on_touch_down=self.place_arrow)

    def update_arrow_position(self, dt):
        if self.placing_arrow and self.arrow_image:
            pos = Window.mouse_pos
            self.arrow_image.pos = (
                pos[0] - self.arrow_image.width / 2,
                pos[1] - self.arrow_image.height / 2,
            )

    def place_arrow(self, instance, touch):
        if self.placing_arrow:
            self.placing_arrow = False
            self.arrow_image.pos = (
                touch.x - self.arrow_image.width / 2,
                touch.y - self.arrow_image.height / 2,
            )
            Clock.unschedule(self.update_arrow_position)
            self.unbind(on_touch_down=self.place_arrow)

            if self.current_arrow_id:
                self.arrow_buttons[self.current_arrow_id]["pos"] = [
                    int(self.arrow_image.pos[0]),
                    int(self.arrow_image.pos[1]),
                ]
            else:
                arrow_id = f"{self.arrow_image.source}_{self.arrow_id_counter}"
                self.arrow_id_counter += 1
                self.arrow_buttons[arrow_id] = {
                    "image": self.arrow_image.source,
                    "pos": [int(self.arrow_image.pos[0]), int(self.arrow_image.pos[1])],
                }
                self.current_arrow_id = arrow_id

            # Popup nur binden, nachdem der Pfeil gesetzt wurde und die Aktion abgeschlossen ist
            Clock.schedule_once(
                lambda dt: self.bind_arrow_to_popup(
                    self.arrow_image, self.current_arrow_id
                ),
                0.1,
            )

            # Speichern der aktuellen Pfeildaten
            self.save_arrows()

    def show_popup_with_id(self, instance, touch, arrow_id):
        if instance.collide_point(*touch.pos) and not self.popup_open:
            self.popup_open = True
            self.current_arrow_id = arrow_id
            popup_layout = BoxLayout(orientation="vertical")
            popup_label = Label(
                text=f"Möchten Sie diesen Punkt {arrow_id} verschieben?"
            )
            popup_layout.add_widget(popup_label)

            button_layout = BoxLayout(size_hint_y=None, height=50)
            btn_yes = Button(text="Ja")
            btn_yes.bind(
                on_release=lambda x: self.enable_arrow_movement(instance, popup)
            )
            btn_no = Button(text="Nein")
            btn_no.bind(on_release=lambda x: self.close_popup(popup))
            button_layout.add_widget(btn_yes)
            button_layout.add_widget(btn_no)

            popup_layout.add_widget(button_layout)

            popup = Popup(
                title="Punkt verschieben",
                content=popup_layout,
                size_hint=(None, None),
                size=(300, 200),
            )
            popup.open()

    def enable_arrow_movement(self, arrow, popup):
        self.close_popup(popup)
        self.placing_arrow = True
        self.arrow_image = arrow
        Clock.schedule_interval(self.update_arrow_position, 0)
        self.bind(on_touch_down=self.place_arrow)

    def close_popup(self, popup):
        popup.dismiss()
        self.popup_open = False

    def save_arrows(self):
        with open(f"{self.current_g_name}.json", "w") as file:
            json.dump(self.arrow_buttons, file)

    def load_arrows(self):
        try:
            with open(f"{self.current_g_name}.json", "r") as file:
                self.arrow_buttons = json.load(file)
                for key, data in self.arrow_buttons.items():
                    arrow_image = Image(
                        size_hint=(None, None),
                        size=(40, 40),
                        fit_mode="scale-down",
                    )
                    arrow_image.pos = data["pos"]
                    self.add_widget(arrow_image)
                    self.bind_arrow_to_popup(arrow_image, key)
        except FileNotFoundError:
            pass

    def bind_arrow_to_popup(self, arrow_image, arrow_id):
        arrow_image.bind(
            on_touch_down=lambda instance, touch: self.show_popup_with_id(
                instance, touch, arrow_id
            )
        )

    def go_back(self, instance):
        self.app.change_Screen("right", "page_2")
