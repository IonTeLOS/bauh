__version__ = '2.0'
__app_name__ = 'waffles'

import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_PATH = '/tmp/{}/logs'.format(__app_name__)
