# popup_new_lkw.py

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty
from kivy.core.window import Window
import json
import os

class Popup_New_Lkw(Popup):
    schaltung = StringProperty('Manuell')

    def __init__(self, lab_txt, **kwargs):
        super().__init__(**kwargs)
        self.txt_lab = lab_txt

        self.title = self.txt_lab['new_truck']
        self.size_hint = (0.75, 0.75)
        
        # Layouts
        layout = BoxLayout(orientation='vertical')
        form_layout = GridLayout(cols=2)
        form_layout.spacing = 10
        self.lab_brand = Label(text=self.txt_lab['brand'])
        self.inp_brand = TextInput(multiline=False, font_size=self.height*0.3)
        self.lab_model = Label(text=self.txt_lab['model'])
        self.inp_model = TextInput(multiline=False, font_size=self.height*0.3)
        self.lab_power = Label(text=self.txt_lab['engine_power'])
        self.inp_power = TextInput(multiline=False, font_size=self.height*0.3)
        
        self.lab_fuel = Label(text=self.txt_lab['fuel_tank_capacity'])
        self.inp_fuel = TextInput(multiline=False, font_size=self.height*0.3)
        self.lab_speed = Label(text=self.txt_lab['top_speed'])
        self.inp_speed = TextInput(multiline=False, font_size=self.height*0.3)
        self.lab_weight = Label(text=self.txt_lab['weight'])
        self.inp_weight = TextInput(multiline=False, font_size=self.height*0.3)
        
        self.lab_f_size = Label(text=self.txt_lab['field_size'])
        self.inp_f_size = TextInput(multiline=False, font_size=self.height*0.3)
        self.lab_payload = Label(text=self.txt_lab['payload'])
        self.inp_payload = TextInput(multiline=False, font_size=self.height*0.3)
        self.lab_price = Label(text=self.txt_lab['purchase_price'])
        self.inp_price = TextInput(multiline=False, font_size=self.height*0.3)
        
        self.lab_path = Label(text=self.txt_lab['img_path'])
        self.inp_path = TextInput(multiline=False, font_size=self.height*0.3)

        form_layout.add_widget(self.lab_brand)
        form_layout.add_widget(self.inp_brand)
        form_layout.add_widget(self.lab_model)
        form_layout.add_widget(self.inp_model)
        form_layout.add_widget(self.lab_power)
        form_layout.add_widget(self.inp_power)
        form_layout.add_widget(self.lab_fuel)
        form_layout.add_widget(self.inp_fuel)
        form_layout.add_widget(self.lab_speed)
        form_layout.add_widget(self.inp_speed)
        form_layout.add_widget(self.lab_weight)
        form_layout.add_widget(self.inp_weight)
        form_layout.add_widget(self.lab_f_size)
        form_layout.add_widget(self.inp_f_size)
        form_layout.add_widget(self.lab_payload)
        form_layout.add_widget(self.inp_payload)
        form_layout.add_widget(self.lab_price)
        form_layout.add_widget(self.inp_price)
        form_layout.add_widget(self.lab_path)
        form_layout.add_widget(self.inp_path)
        
        
        
        
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
        Window.bind(on_key_down=self._on_key_down)
        
    def _on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 43 or keycode == 40:  # Tab key
            if self.inp_brand.focus:
                self.inp_model.focus = True
            elif self.inp_model.focus:
                self.inp_power.focus = True
            elif self.inp_power.focus:
                self.inp_fuel.focus = True
            elif self.inp_fuel.focus:
                self.inp_speed.focus = True
            elif self.inp_speed.focus:
                self.inp_weight.focus = True
            elif self.inp_weight.focus:
                self.inp_f_size.focus = True
            elif self.inp_f_size.focus:
                self.inp_payload.focus = True
            elif self.inp_payload.focus:
                self.inp_price.focus = True
            elif self.inp_price.focus:
                self.inp_path.focus = True
            elif self.inp_path.focus:
                self.inp_brand.focus = True
            return True
        return False

    
    def save_data(self, instance):
        data = {self.lab_brand.text: self.inp_brand.text, 
                self.lab_model.text: self.inp_model.text,
                self.lab_power.text: self.inp_power.text,
                self.lab_fuel.text: self.inp_fuel.text,
                self.lab_speed.text: self.inp_speed.text,
                self.lab_weight.text: self.inp_weight.text,
                self.lab_f_size.text: self.inp_f_size.text,
                self.lab_payload.text: self.inp_payload.text,
                self.lab_price.text: self.inp_price.text,
                self.lab_path.text: self.inp_path.text}
        if self.manuell_checkbox.active:
            data['Schaltung'] = 'Manuell'
        else:
            data['Schaltung'] = 'Automatik'
        
        # Load existing data with error handling
        existing_data = {}
        if os.path.exists('files_data/data_lkw.json'):
            try:
                with open('files_data/data_lkw.json', 'r') as f:
                    existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {}
        
        # Determine new vehicle ID
        new_id = str(len(existing_data) + 1)
        
        # Add new data to existing data
        existing_data[new_id] = data
        
        # Save updated data
        with open('files_data/data_lkw.json', 'w') as f:
            json.dump(existing_data, f, indent=4)
        
        self.dismiss()