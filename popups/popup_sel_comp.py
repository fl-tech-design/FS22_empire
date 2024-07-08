from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import os

class CompanySelectionPopup(Popup):
    def __init__(self, lab_txt, **kwargs):
        super(CompanySelectionPopup, self).__init__(**kwargs)
        self.title = "Select a Company"
        self.txt_lab = lab_txt
        # Layout for the popup
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Grid layout for company images
        self.grid = GridLayout(cols=3, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        
        scrollview = ScrollView(size_hint=(1, None), size=(400, 300))
        scrollview.add_widget(self.grid)

        # Load images from the folder
        image_folder = 'app_pics/img_companies'
        for img_file in os.listdir(image_folder):
            if img_file.endswith('.png'):
                img_path = os.path.join(image_folder, img_file)
                img_button = Button(size_hint_y=None, height=100)
                img_button.background_normal = img_path
                img_button.background_down = img_path
                img_button.bind(on_release=self.on_image_select)
                self.grid.add_widget(img_button)

        # Text input for company name
        name_label = Label(text="Enter Company Name:")
        self.company_name_input = TextInput(multiline=False, size_hint_y=None, height=30)

        # Buttons for confirming or cancelling the selection
        button_layout = BoxLayout(size_hint_y=None, height=50)
        select_button = Button(text="Select")
        select_button.bind(on_release=self.on_select)
        cancel_button = Button(text="Cancel")
        cancel_button.bind(on_release=self.dismiss)
        
        button_layout.add_widget(select_button)
        button_layout.add_widget(cancel_button)

        # Add widgets to the layout
        layout.add_widget(scrollview)
        layout.add_widget(name_label)
        layout.add_widget(self.company_name_input)
        layout.add_widget(button_layout)

        self.content = layout

    def on_image_select(self, instance):
        self.selected_image = instance.background_normal

    def on_select(self, instance):
        company_name = self.company_name_input.text
        selected_image = getattr(self, 'selected_image', None)
        if company_name and selected_image:
            print(f"Selected Company: {company_name}")
            print(f"Selected Image: {selected_image}")
        self.dismiss()


