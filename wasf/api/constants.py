import os
from pathlib import Path

CACHE_PATH = '{}/.cache/wasf'.format(str(Path.home()))
CONFIG_PATH = '{}/.config/wasf'.format(str(Path.home()))
USER_THEMES_PATH = '{}/.local/share/wasf/themes'.format(str(Path.home()))
DESKTOP_ENTRIES_DIR = '{}/.local/share/applications'.format(str(Path.home()))
TEMP_DIR = '/tmp/wasf{}'.format('_root' if os.getuid() == 0 else '')
