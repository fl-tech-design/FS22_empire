#constants.py
import os

VERSION_NR = '0.0.8'

# Paths to dirs
DIR_FONTS = os.path.join(os.path.dirname(__file__), 'app_fonts/')
DIR_POPUPS = os.path.join(os.path.dirname(__file__), 'popups/')
DIR_LOGOS = os.path.join(os.path.dirname(__file__), 'files_data/data_game/img_logos/')

DIR_SIGNS = os.path.join(os.path.dirname(__file__), 'files_data/data_game/game_signs/')

DIR_MAPS = os.path.join(os.path.dirname(__file__), 'files_data/data_game/maps/')


# Paths to images
PATH_TO_MAINLOGO = DIR_LOGOS + 'logo_fs22-empire.png'


# Path splashscreens
SPL_SCREEN_START_APP = os.path.join(os.path.dirname(__file__), 'app_pics/app_splashscreens/spl_giants.jpg')


# Paths datafiles
PATH_DATA_APP = os.path.join(os.path.dirname(__file__), 'files_data/data_app.json')
PATH_DATA_TXT = os.path.join(os.path.dirname(__file__), 'files_data/data_txt.json')
PATH_DATA_GAME = os.path.join(os.path.dirname(__file__), 'files_data/data_game.json')
PATH_DIR_U_DAT = os.path.join(os.path.dirname(__file__),'files_data/data_userfiles/')

# Paths .kv-files

PATH_KV_STARTPAGE = os.path.join(os.path.dirname(__file__), 'pages/page_start/startpage.kv')
PATH_KV_SETTINGPAGE = os.path.join(os.path.dirname(__file__), 'pages/page_settings/settingpage.kv')
PATH_KV_PAGE_4 = os.path.join(os.path.dirname(__file__), 'pages/page_buy_item/pagebuyitem.kv')
PATH_KV_PAGEMAINGAME = os.path.join(os.path.dirname(__file__), 'pages/page_main_game/pagemaingame.kv')
PATH_KV_PAGEGAMEMAP = os.path.join(os.path.dirname(__file__), 'pages/page_game_map/page_game_map.kv')

PATH_KV_COLORS = os.path.join(os.path.dirname(__file__), 'files_kv/colors.kv')
PATH_KV_BOXES = os.path.join(os.path.dirname(__file__), 'files_kv/boxes.kv')
PATH_KV_COMPONENTS = os.path.join(os.path.dirname(__file__), 'files_kv/components.kv')
PATH_KV_WIDGETS = os.path.join(os.path.dirname(__file__), 'files_kv/widgets.kv')


# constants fonts
TITLEFONT = 'Jura-DemiBold.otf'
LABELFONT_M = 'Jura-Medium.otf'

BUT_CLEAR = os.path.join(os.path.dirname(__file__), 'app_pics/img_clear.png')


LOG_FILE = os.path.join(os.path.dirname(__file__), 'files_data/error_log.txt')