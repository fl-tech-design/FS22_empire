# popup_new_lkw.py

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty
import json
import os

class Popup_New_Tractor(Popup):
    schaltung = StringProperty('Manuell')

    def __init__(self, lab_txt, **kwargs):
        super().__init__(**kwargs)
        self.txt_lab = lab_txt

        self.title = self.txt_lab['new_tractor']
        self.size_hint = (0.75, 0.75)
        
        # Layouts
        layout = BoxLayout(orientation='vertical')
        form_layout = GridLayout(cols=2)
        form_layout.spacing = 10
        
        # Labels and TextInputs
        self.inputs = {
            'Marke': TextInput(multiline=False, font_size=self.height*0.3),
            'Modell': TextInput(multiline=False, font_size=self.height*0.3),
            'Leistung': TextInput(multiline=False, font_size=self.height*0.3),
            'Tankvolumen': TextInput(multiline=False, font_size=self.height*0.3),
            'Höchstgeschwindigkeit': TextInput(multiline=False, font_size=self.height*0.3),
            'Gewicht': TextInput(multiline=False, font_size=self.height*0.3),
            'Feldergröße': TextInput(multiline=False, font_size=self.height*0.3),
            'Nutzlast': TextInput(multiline=False, font_size=self.height*0.3)
        }
        
        for label, text_input in self.inputs.items():
            form_layout.add_widget(Label(text=label))
            form_layout.add_widget(text_input)
        
        # Radiobuttons for Schaltung
        form_layout.add_widget(Label(text='Schaltung'))

        radio_layout = BoxLayout()
        manuell_box = BoxLayout(orientation='horizontal')
        automatik_box = BoxLayout(orientation='horizontal')

        manuell_label = Label(text='Manuell')
        automatik_label = Label(text='Automatik')

        self.manuell_checkbox = CheckBox(group='schaltung', active=True)
        self.automatik_checkbox = CheckBox(group='schaltung')

        manuell_box.add_widget(manuell_label)
        manuell_box.add_widget(self.manuell_checkbox)
        
        automatik_box.add_widget(automatik_label)
        automatik_box.add_widget(self.automatik_checkbox)
        
        radio_layout.add_widget(manuell_box)
        radio_layout.add_widget(automatik_box)
        
        form_layout.add_widget(radio_layout)
        
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
        if self.manuell_checkbox.active:
            data['Schaltung'] = 'Manuell'
        else:
            data['Schaltung'] = 'Automatik'
        
        # Load existing data
        if os.path.exists('files_data/data_tractor.json'):
            with open('files_data/data_tractor.json', 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = {}
        
        # Determine new vehicle ID
        new_id = str(len(existing_data) + 1)
        
        # Add new data to existing data
        existing_data[new_id] = data
        
        # Save updated data
        with open('files_data/data_tractor.json', 'w') as f:
            json.dump(existing_data, f, indent=4)
        
        self.dismiss()
