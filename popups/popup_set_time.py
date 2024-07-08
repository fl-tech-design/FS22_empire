# popup_set_time.py

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TimePopup(Popup):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Zeit einstellen'
        self.size_hint = (0.8, 0.8)

        self.callback = callback

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.hours_input = TextInput(hint_text='Stunden', multiline=False, input_filter='int')
        self.minutes_input = TextInput(hint_text='Minuten', multiline=False, input_filter='int')

        self.layout.add_widget(Label(text='Stunden:'))
        self.layout.add_widget(self.hours_input)
        self.layout.add_widget(Label(text='Minuten:'))
        self.layout.add_widget(self.minutes_input)

        self.ok_button = Button(text='OK', on_press=self.on_ok_pressed, disabled=True)
        self.layout.add_widget(self.ok_button)

        self.add_widget(self.layout)

        self.hours_input.bind(text=self.on_text_input)
        self.minutes_input.bind(text=self.on_text_input)

    def on_text_input(self, instance, value):
        if self.hours_input.text and self.minutes_input.text:
            self.ok_button.disabled = False
        else:
            self.ok_button.disabled = True

    def on_ok_pressed(self, instance):
        hours = int(self.hours_input.text)
        minutes = int(self.minutes_input.text)
        self.callback(hours, minutes)
        self.dismiss()
