from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import os

from constants import *

kv_path = os.path.join(os.path.dirname(__file__), "buyitempage.kv")
Builder.load_file(kv_path)


class BuyItemPage(Screen):
    def __init__(self, app, **kwargs):
        super(BuyItemPage, self).__init__(**kwargs)
        self.app = app
        self.truck_index = 0
        self.truck_data = {}

    def update_labels(self):
        self.truck_data = self.app.data_trucks[
            str(self.truck_index + 1)
        ]  # JSON keys are strings
        self.check_Brand()
        list_data_truck = list(self.truck_data.keys())

        self.ids.box_title.ids.lab_tit.text = self.app.lab_txt["buy_a_new_truck"]

        self.ids.lab_key_brand.text = list_data_truck[0]
        self.ids.lab_val_brand.text = self.truck_data[list_data_truck[0]]
        self.ids.lab_key_model.text = list_data_truck[1]
        self.ids.lab_val_model.text = self.truck_data[list_data_truck[1]]
        self.ids.lab_key_power.text = list_data_truck[2]
        self.ids.lab_val_power.text = self.truck_data[list_data_truck[2]]
        self.ids.lab_key_fuel.text = list_data_truck[3]
        self.ids.lab_val_fuel.text = self.truck_data[list_data_truck[3]]

        self.ids.but_buy.text = self.app.lab_txt["buy"]

        self.ids.img_show_truck.source = PATH_TO_TRUCK_IMG + self.truck_data["img_path"]

    def check_Brand(self):
        if self.truck_data["Marke"] == "FIAT":
            self.ids.img_brand.source = self.app.data_app["data_logo_brands"]["fiat"]
        elif self.truck_data["Marke"] == "INTERNATIONAL":
            self.ids.img_brand.source = self.app.data_app["data_logo_brands"][
                "international"
            ]
        elif self.truck_data["Marke"] == "LIZARD":
            self.ids.img_brand.source = self.app.data_app["data_logo_brands"]["lizard"]
        elif self.truck_data["Marke"] == "MACK":
            self.ids.img_brand.source = self.app.data_app["data_logo_brands"]["mack"]
        elif self.truck_data["Marke"] == "MAN":
            self.ids.img_brand.source = self.app.data_app["data_logo_brands"]["man"]
        elif self.truck_data["Marke"] == "Tatra":
            self.ids.img_brand.source = self.app.data_app["data_logo_brands"]["tatra"]
        elif self.truck_data["Marke"] == "Volvo":
            self.ids.img_brand.source = self.app.data_app["data_logo_brands"]["volvo"]

    def incr_curr_index(self):
        if self.truck_index < len(self.app.data_trucks) - 1:
            self.truck_index += 1
        else:
            self.truck_index = len(self.app.data_trucks) - 1

    def decr_curr_index(self):
        if self.truck_index > 0:
            self.truck_index -= 1
        else:
            self.truck_index = 0
