#constants.py
import os

VERSION_NR = '0.0.5'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to dirs
DIR_FONTS = os.path.join(os.path.dirname(__file__), 'app_fonts/')
DIR_IMAGES = os.path.join(os.path.dirname(__file__), 'app_pics/')
DIR_POPUPS = os.path.join(os.path.dirname(__file__), 'popups/')
DIR_MAPS = os.path.join(os.path.dirname(__file__), 'app_pics/')

# Paths to images
SPL_SCREEN_START_APP = DIR_IMAGES + 'img_spl_giants.jpg'
PATH_TO_MAINLOGO = os.path.join(os.path.dirname(__file__), 'app_pics/img_logo_fs22-empire.png')
PATH_TO_TRUCK_IMG = os.path.join(os.path.dirname(__file__), 'app_pics/')
PATH_DIR_IMG_CHO = os.path.join(os.path.dirname(__file__), 'app_pics/img_cho_map/')


# Paths datafiles
PATH_DATA_APP = os.path.join(os.path.dirname(__file__), 'files_data/data_app.json')
PATH_DATA_TXT = os.path.join(os.path.dirname(__file__), 'files_data/data_txt.json')
PATH_DATA_GAME = os.path.join(os.path.dirname(__file__), 'files_data/data_game.json')
DF_TRUCKS = os.path.join(os.path.dirname(__file__), 'files_data/data_lkw.json')
DF_USER = os.path.join(os.path.dirname(__file__),'files_data/user_data.json')

# Paths .kv-files

PATH_KV_STARTPAGE = os.path.join(os.path.dirname(__file__), 'pages/startpage/startpage.kv')
PATH_KV_SETTINGPAGE = os.path.join(os.path.dirname(__file__), 'pages/settingpage/settingpage.kv')
PATH_KV_PAGE_4 = os.path.join(os.path.dirname(__file__), 'pages/buyitempage/buyitempage.kv')


PATH_KV_COLORS = os.path.join(os.path.dirname(__file__), 'files_kv/colors.kv')
PATH_KV_BOXES = os.path.join(os.path.dirname(__file__), 'files_kv/boxes.kv')
PATH_KV_COMPONENTS = os.path.join(os.path.dirname(__file__), 'files_kv/components.kv')
PATH_KV_WIDGETS = os.path.join(os.path.dirname(__file__), 'files_kv/widgets.kv')


# constants fonts
TITLEFONT = 'Jura-DemiBold.otf'
LABELFONT_M = 'Jura-Medium.otf'

