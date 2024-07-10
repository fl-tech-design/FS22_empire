import json
import os
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
        with open(DF_TRUCKS, 'r', encoding='utf-8') as f:
            trucks = json.load(f)
        return trucks

    def create_Save_File(self, curr_name: str, curr_map: str, saved_games: dict):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Erstelle den Dateinamen mit dem Benutzernamen und dem aktuellen Datum/Uhrzeit
        filename = f"game_saves/{curr_name}_{now}.json"
        # datadict for gamesave
        gamesave_data = {
            'username': curr_name,
            'map': curr_map,
            'save_state': 1,
            'creation_date': now,
            'last_save': now,
            'garage': {},
            'companies': {},
            'delivery_notes': {},
            'file_name': filename
        }
        # Schreibe das Dictionary in eine JSON-Datei
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(gamesave_data, json_file, indent=4, ensure_ascii=False)
        saved_games.append(f'{gamesave_data["username"]}_{gamesave_data["map"]}')
        self.set_Data_App('saved_games', saved_games)
    
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

    def remove_empty_list_item(self, userliste, neuer_uname):
        if "" in userliste:
            index = userliste.index("")
            userliste[index] = neuer_uname
        return userliste

    def get_curr_player_data(self, curr_player_name: str):
        try:
            with open(DF_USER, "r", encoding="utf-8") as datei:
                daten = json.load(datei)
            return daten[curr_player_name]
        except FileNotFoundError as fe:
            print(f"Die {fe} wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Die Datei ist keine gültige JSON-Datei.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return None

