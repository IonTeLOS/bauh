from waffles.commons.config import YAMLConfigManager
from waffles.gems.appimage import CONFIG_FILE


class AppImageConfigManager(YAMLConfigManager):

    def __init__(self):
        super(AppImageConfigManager, self).__init__(config_file_path=CONFIG_FILE)

    def get_default_config(self) -> dict:
        return {
            'database': {
                'expiration': 3600
            },
            'suggestions': {
                'expiration': 120
            }
        }
