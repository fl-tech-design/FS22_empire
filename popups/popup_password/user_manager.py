# user_manager.py
import json
import bcrypt

from constants import *


def load_user_data():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_user_data(user_data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(user_data, file)


def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def check_password(stored_password, provided_password):
    return bcrypt.checkpw(
        provided_password.encode("utf-8"), stored_password.encode("utf-8")
    )


def register_user(username, password):
    now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    user_data = load_user_data()
    if username in user_data:
        return False  # User already exists
    user_data[username] = {
        "password": hash_password(password),
        "creation_date": now,
        "last_save": now,
        "saved_games": 0,
        "played_games": 0,
        "last_game": "",
        "tot_p_time": "0h 0min",
        "saved_games_data": [
            {
                "map_name": "",
                "creation_date": "",
                "time_scale": 1,
                "days_per_month": 1,
                "total_cash": 0,
                "my_vehicles": {},
                "my_factories": {},
                "my_devices": {},
            },
            {
                "map_name": "",
                "creation_date": "",
                "time_scale": 1,
                "days_per_month": 1,
                "total_cash": 0,
                "my_vehicles": {},
                "my_factories": {},
                "my_devices": {},
            },
            {
                "map_name": "",
                "creation_date": "",
                "time_scale": 1,
                "days_per_month": 1,
                "total_cash": 0,
                "my_vehicles": {},
                "my_factories": {},
                "my_devices": {},
            },
            {
                "map_name": "",
                "creation_date": "",
                "time_scale": 1,
                "days_per_month": 1,
                "total_cash": 0,
                "my_vehicles": {},
                "my_factories": {},
                "my_devices": {},
            },
            {
                "map_name": "",
                "creation_date": "",
                "time_scale": 1,
                "days_per_month": 1,
                "total_cash": 0,
                "my_vehicles": {},
                "my_factories": {},
                "my_devices": {},
            },
        ],
    }
    save_user_data(user_data)
    return True


def validate_user(username, password):
    user_data = load_user_data()
    if username in user_data and check_password(
        user_data[username]["password"], password
    ):
        return True
    return False
