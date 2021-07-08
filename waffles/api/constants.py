import os
from pathlib import Path

CACHE_PATH = '{}/.cache/waffles'.format(str(Path.home()))
CONFIG_PATH = '{}/.config/waffles'.format(str(Path.home()))
USER_THEMES_PATH = '{}/.local/share/waffles/themes'.format(str(Path.home()))
DESKTOP_ENTRIES_DIR = '{}/usr/share/applications'.format(str(Path.home()))
TEMP_DIR = '/tmp/waffles{}'.format('_root' if os.getuid() == 0 else '')
