from pathlib import Path

from waffles import __app_name__
from waffles.commons.config import YAMLConfigManager

FILE_PATH = '{}/.config/{}/config.yml'.format(str(Path.home()), __app_name__)


class CoreConfigManager(YAMLConfigManager):

    def __init__(self):
        super(CoreConfigManager, self).__init__(config_file_path=FILE_PATH)

    def get_default_config(self) -> dict:
        return {
            'gems': None,
            'memory_cache': {
                'data_expiration': 60 * 60,
                'icon_expiration': 60 * 30
            },
            'locale': None,
            'updates': {
                'check_interval': 3600,
                'ask_for_reboot': False
            },
            'system': {
                'notifications': True,
                'single_dependency_checking': False
            },
            'suggestions': {
                'enabled': True,
                'by_type': 30
            },
            'ui': {
                'table': {
                    'max_displayed': 120
                },
                'tray': {
                    'default_icon': None,
                    'updates_icon': None
                },
                'qt_style': 'fusion',
                'hdpi': True,
                "auto_scale": False,
                "scale_factor": 1.0,
                'theme': 'darcula',
                'system_theme': False

            },
            'download': {
                'multithreaded': True,
                'multithreaded_client': None,
                'icons': True
            },
            'store_root_password': True,
            'boot': {
                'load_apps': True
            }
        }
