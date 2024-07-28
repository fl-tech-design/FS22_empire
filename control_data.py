import json
from datetime import datetime
import os
from constants import PATH_DATA_APP, PATH_DATA_TXT, DIR_MAPS, PATH_DIR_U_DAT, LOG_FILE


class DataControl:
    def __init__(self, app, **kwargs) -> None:
        """
        Initialisierung der Variabeln.
        """
        self.app = app

    # 23.07.24
    def return_Data_App(self):
        """
        Loads application data from a JSON file.

        Returns:
            dict: A dictionary containing the application data loaded from the JSON file.
                Returns an empty dictionary if there is an error loading the data.

        This function reads a JSON file specified by `PATH_DATA_APP` and loads the
        application data into a dictionary. This data is used for the core functionality
        of the application. If an error occurs while reading the file (e.g., file not
        found or JSON decoding error), the function logs the error and returns an empty
        dictionary. Note that game-specific data is handled by a separate function.
        """
        try:
            with open(PATH_DATA_APP, "r", encoding="utf-8") as datei:
                daten = json.load(datei)
            return daten
        except FileNotFoundError as f_err:
            self.log_error(f_err)
        except json.JSONDecodeError as dec_err:
            self.log_error(dec_err)
        except Exception as exp_err:
            self.log_error(exp_err)
            return {}

    # 23.07.24
    def return_Lab_Txt(self, curr_language: str) -> dict:
        """
        Loads label texts from a JSON file based on the specified current language.

        Args:
            curr_language (str): The language code indicating the desired language of the labels.

        Returns:
            dict or None: A dictionary containing label texts in the specified language.
                Returns None if there is an error loading the data.

        This function reads a JSON file containing label texts for different languages.
        It retrieves and returns the dictionary of labels corresponding to the provided
        `curr_language`. This function is intended to be used in multilingual applications
        to dynamically update all labels when the language setting changes. If the specified
        language file is not found or there is an issue decoding the JSON data, it logs
        the error and returns None.
        """
        try:
            with open(PATH_DATA_TXT, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data[curr_language]
        except FileNotFoundError as f_err:
            self.log_error(f_err)
        except json.JSONDecodeError as dec_err:
            self.log_error(dec_err)
        except Exception as exp_err:
            self.log_error(exp_err)
            return {}

    # 23.07.24
    def load_All_Maps(self, map_name):
        """
        Loads map data for the game from JSON files based on the provided map names.

        Args:
            map_names (list): A list of map names for which the data should be loaded.

        Returns:
            dict: A dictionary where each key is a map name from `map_names`, and the value
                is the corresponding map data loaded from a JSON file. Returns an empty
                dictionary if there is an error loading any map data.
        """
        json_filename = f"{DIR_MAPS}{map_name}/{map_name}.json"
        try:
            with open(json_filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError as f_err:
            self.log_error(f_err)
        except json.JSONDecodeError as dec_err:
            self.log_error(dec_err)
        except Exception as exp_err:
            self.log_error(exp_err)

    # 23.07.24
    def set_Data_App(self, data_key: str, data_value: str) -> None:
        """
        Updates a specific entry in the application data JSON file.

        Args:
            data_key (str): The key in the JSON data that needs to be updated.
            data_value (str): The new value to be assigned to the specified key.

        Returns:
            None: This function does not return a value.

        This function reads the application data from a JSON file specified by `PATH_DATA_APP`,
        updates the value associated with the provided `data_key` to `data_value`, and writes
        the updated data back to the file. If there is an error reading or writing the file
        (e.g., file not found or JSON decoding error), the function logs the error. This function
        does not return a value and will modify the data directly in the JSON file.
        """
        try:
            with open(PATH_DATA_APP, "r", encoding="utf-8") as file:
                data = json.load(file)
            data[data_key] = data_value
            with open(PATH_DATA_APP, "w", encoding="utf-8") as file:
                json.dump(data, file)
        except FileNotFoundError as f_err:
            self.log_error(f_err)
        except json.JSONDecodeError as dec_err:
            self.log_error(dec_err)
        except Exception as exp_err:
            self.log_error(exp_err)

    # 23.07.24
    def set_Uname_List(self, list_index: int, new_uname: str) -> None:
        """
        Updates a specific entry in the application data JSON file.

        Args:
            data_key (str): The key in the JSON data that needs to be updated.
            data_value (str): The new value to be assigned to the specified key.

        Returns:
            None: This function does not return a value.

        This function reads the application data from a JSON file specified by `PATH_DATA_APP`,
        updates the value associated with the provided `data_key` to `data_value`, and writes
        the updated data back to the file. If there is an error reading or writing the file
        (e.g., file not found or JSON decoding error), the function logs the error. This function
        does not return a value and will modify the data directly in the JSON file.
        """
        try:
            with open(PATH_DATA_APP, "r", encoding="utf-8") as file:
                data = json.load(file)
            data["user_list"][list_index] = new_uname
            with open(PATH_DATA_APP, "w", encoding="utf-8") as file:
                json.dump(data, file)
        except FileNotFoundError as f_err:
            self.log_error(f_err)
        except json.JSONDecodeError as dec_err:
            self.log_error(dec_err)
        except Exception as exp_err:
            self.log_error(exp_err)

    # 23.07.24
    def set_Last_Login(self, curr_uname: str) -> None:
        """
        Updates the last login timestamp for the specified user.

        Args:
            curr_uname (str): The u_name of the current user.

        Returns:
            None: This function does not return a value.

        This function updates the "last_login" timestamp in the user's data JSON file
        with the current date and time. The JSON file is specified by `curr_uname` and
        is located in the directory specified by `PATH_DIR_U_DAT`. After updating the
        file, the function refreshes the application's current user data by calling
        `self.ret_User_Data`. If there is an error reading or writing the file
        (e.g., file not found or JSON decoding error), the function logs the error.
        """
        now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        try:
            with open(
                f"{PATH_DIR_U_DAT}{curr_uname}.json", "r", encoding="utf-8"
            ) as file:
                data = json.load(file)
            data["last_login"] = now
            with open(
                f"{PATH_DIR_U_DAT}{curr_uname}.json", "w", encoding="utf-8"
            ) as file:
                json.dump(data, file)
            self.app.user_data = self.ret_User_Data(curr_uname)
        except FileNotFoundError as f_err:
            self.log_error(f_err)
        except json.JSONDecodeError as dec_err:
            self.log_error(dec_err)
        except Exception as exp_err:
            self.log_error(exp_err)

    def read_Curr_Map_Data(self, curr_map: str):
        if curr_map:
            try:
                with open(f"{DIR_MAPS}{curr_map}", "r", encoding="utf-8") as datei:
                    daten = json.load(datei)
                return daten
            except FileNotFoundError as f_err:
                self.log_error(f_err)
            except json.JSONDecodeError as dec_err:
                self.log_error(dec_err)
            except Exception as exp_err:
                self.log_error(exp_err)
                return {}

    def log_error(self, message: str):

        timestamp = datetime.now().strftime("%y.%m.%d_%H:%M.%S")
        log_message = f"{timestamp} - ERROR - {message}\n"

        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "a") as file:
                file.write(log_message)
        else:
            with open(LOG_FILE, "w") as file:
                file.write(log_message)

    def load_User_Data(self, user_name: str) -> dict:
        """
        Loads user data from a JSON file based on the provided u_name.

        Args:
            curr_uname (str): The u_name of the user whose data needs to be loaded.

        Returns:
            dict: A dictionary containing the user's data loaded from the JSON file.
                Returns an empty dictionary if there is an error loading the data.

        This function reads the user's data from a JSON file located in the directory
        specified by `PATH_DIR_U_DAT`, with the filename being `{curr_uname}.json`.
        If the file is successfully read, it returns the data as a dictionary. In case
        of an error (e.g., file not found or JSON decoding error), it logs the error
        and returns an empty dictionary.
        """
        try:
            with open(f"{PATH_DIR_U_DAT}{user_name}.json", "r") as file:
                return json.load(file)
        except FileNotFoundError as f_err:
            DataControl.log_error(f_err)
            return {}
