# popups/geraete_popup.py

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import json
import os

class GeraetePopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Neues Gerät"
        self.size_hint = (0.75, 0.75)
        
        # Layouts
        layout = BoxLayout(orientation='vertical')
        form_layout = GridLayout(cols=2)
        
        # Labels and TextInputs
        self.inputs = {
            'Name': TextInput(multiline=False),
            'Typ': TextInput(multiline=False),
            'Leistung': TextInput(multiline=False),
            'Gewicht': TextInput(multiline=False),
            'Preis': TextInput(multiline=False)
        }
        
        for label, text_input in self.inputs.items():
            form_layout.add_widget(Label(text=label))
            form_layout.add_widget(text_input)
        
        layout.add_widget(form_layout)
        
        # Buttons
        button_layout = BoxLayout(size_hint_y=0.2)
        save_button = Button(text='Speichern')
        cancel_button = Button(text='Abbrechen')
        
        save_button.bind(on_press=self.save_data)
        cancel_button.bind(on_press=self.dismiss)
        
        button_layout.add_widget(save_button)
        button_layout.add_widget(cancel_button)
        
        layout.add_widget(button_layout)
        
        self.add_widget(layout)
    
    def save_data(self, instance):
        data = {key: text_input.text for key, text_input in self.inputs.items()}
        
        # Load existing data
        if os.path.exists('geraete.json'):
            with open('geraete.json', 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = {}
        
        # Determine new device ID
        new_id = str(len(existing_data) + 1)
        
        # Add new data to existing data
        existing_data[new_id] = data
        
        # Save updated data
        with open('geraete.json', 'w') as f:
            json.dump(existing_data, f, indent=4)
        
        self.dismiss()
