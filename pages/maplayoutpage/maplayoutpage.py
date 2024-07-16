#maplayoutpage.py
from kivy.uix.screenmanager import Screen
from pages.page_map.mappage import PageMap

class PageMapLayout(Screen):
    def __init__(self, app, **kwargs):
        super(PageMapLayout, self).__init__(**kwargs)
        self.map_layout = PageMap(app.lab_txt, app)
        self.add_widget(self.map_layout)
