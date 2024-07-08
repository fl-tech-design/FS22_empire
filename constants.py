#constants.py
import os

VERSION_NR = '1.0.0'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


FONT_DIR = os.path.join(os.path.dirname(__file__), 'app_fonts/')
IMG_DIR = os.path.join(os.path.dirname(__file__), 'app_pics/')
IMG_POPUPS = os.path.join(os.path.dirname(__file__), 'popups/')

PATH_SPLASHSCREEN = IMG_DIR + "bg_giants.jpg"


PATH_DATA_APP = os.path.join(os.path.dirname(__file__), 'files_data/data_app.json')
PATH_DATA_TXT = os.path.join(os.path.dirname(__file__), 'files_data/data_txt.json')
PATH_DATA_GAME = os.path.join(os.path.dirname(__file__), 'files_data/data_game.json')
PATH_DIR_MAPS = os.path.join(os.path.dirname(__file__), 'app_pics/')


PATH_TO_MAINLOGO = os.path.join(os.path.dirname(__file__), 'app_pics/img_fs22-empire.png')
PATH_TO_TRUCK_IMG = os.path.join(os.path.dirname(__file__), 'app_pics/')
PATH_TO_TRUCK_DATA = os.path.join(os.path.dirname(__file__), 'files_data/data_lkw.json')


PATH_KV_STARTPAGE = os.path.join(os.path.dirname(__file__), 'pages/startpage/startpage.kv')
PATH_KV_SETTINGPAGE = os.path.join(os.path.dirname(__file__), 'pages/settingpage/settingpage.kv')
PATH_KV_PAGE_4 = os.path.join(os.path.dirname(__file__), 'pages/page4/page4.kv')

USER_DATA_FILE = os.path.join(os.path.dirname(__file__),'files_data/user_data.json')

PATH_KV_COLORS = os.path.join(os.path.dirname(__file__), "files_kv/colors.kv")
PATH_KV_BOXES = os.path.join(os.path.dirname(__file__), "files_kv/boxes.kv")
PATH_KV_COMPONENTS = os.path.join(os.path.dirname(__file__), "files_kv/components.kv")
PATH_KV_WIDGETS = os.path.join(os.path.dirname(__file__), "files_kv/widgets.kv")




