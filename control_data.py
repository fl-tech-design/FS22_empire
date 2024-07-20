import json
from datetime import datetime
from constants import *


class DataControl:
    def __init__(self, app, **kwargs) -> None:
        """
        Initialisierung der Variabeln.
        """
        self.app = app

    def read_data_app(self):
        try:
            with open(PATH_DATA_APP, "r", encoding="utf-8") as datei:
                daten = json.load(datei)
            return daten
        except FileNotFoundError as fe:
            print(f"Die {fe} wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Die Datei ist keine gültige JSON-Datei.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return None

    def read_data_game(self):
        try:
            with open(PATH_DATA_GAME, "r", encoding="utf-8") as datei:
                daten = json.load(datei)
            return daten
        except FileNotFoundError as fe:
            print(f"Die {fe} wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Die Datei ist keine gültige JSON-Datei.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return None

    def read_data_txt(self, curr_language):
        try:
            with open(PATH_DATA_TXT, "r", encoding="utf-8") as datei:
                daten = json.load(datei)
            return daten[curr_language]
        except FileNotFoundError as fe:
            print(f"Die {fe} wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Die Datei ist keine gültige JSON-Datei.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return None

    def load_trucks_from_json(self):
        with open(DF_TRUCKS, "r", encoding="utf-8") as f:
            trucks = json.load(f)
        return trucks

    def set_Data_App(self, data_key: str, data_value: str) -> None:
        """
        Updates the application configuration data in the app_config.json file.
        :param data_key: The key of the configuration data to update.
        :type data_key: str
        :param data_value: The new value to set for the configuration data.
        :type data_value: str
        :return: None
        """
        with open(PATH_DATA_APP, "r", encoding="utf-8") as file:
            data = json.load(file)
        data[data_key] = data_value
        with open(PATH_DATA_APP, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def set_Last_Login(self, curr_uname: str) -> None:
        """
        Updates the application configuration data in the app_config.json file.
        :param data_key: The key of the configuration data to update.
        :type data_key: str
        :param data_value: The new value to set for the configuration data.
        :type data_value: str
        :return: None
        """
        now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        with open(PATH_USER_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
        data[curr_uname]["last_login"] = now
        with open(PATH_USER_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file)
        self.app.curr_u_data = self.get_curr_player_data(curr_uname)

    def remove_empty_list_item(self, userliste: list, neuer_uname: str):
        if "" in userliste:
            index = userliste.index("")
            userliste[index] = neuer_uname
        return userliste

    def read_Curr_Map_Data(self, curr_map: str):
        try:
            with open(f"{DIR_MAPS}{curr_map}", "r", encoding="utf-8") as datei:
                daten = json.load(datei)
            return daten
        except FileNotFoundError as fe:
            print(f"Die {fe} wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Die Datei ist keine gültige JSON-Datei.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return None

    def get_curr_player_data(self, curr_player_name: str):
        try:
            with open(PATH_USER_DATA, "r", encoding="utf-8") as datei:
                daten = json.load(datei)
            return daten[curr_player_name]
        except FileNotFoundError as fe:
            print(f"Die {fe} wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Die Datei ist keine gültige JSON-Datei.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return None
