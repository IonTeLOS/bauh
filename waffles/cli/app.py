import os

import urllib3

from waffles import ROOT_DIR
from waffles.api.abstract.context import ApplicationContext
from waffles.api.http import HttpClient
from waffles.cli import __app_name__, cli_args
from waffles.cli.controller import CLIManager
from waffles.commons.internet import InternetChecker
from waffles.context import generate_i18n, DEFAULT_I18N_KEY
from waffles.view.core import gems
from waffles.view.core.config import CoreConfigManager
from waffles.view.core.controller import GenericSoftwareManager
from waffles.view.core.downloader import AdaptableFileDownloader
from waffles.view.util import logs, util, resource
from waffles.view.util.cache import DefaultMemoryCacheFactory
from waffles.view.util.disk import DefaultDiskCacheLoaderFactory


def main():
    if not os.getenv('PYTHONUNBUFFERED'):
        os.environ['PYTHONUNBUFFERED'] = '1'

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    args = cli_args.read()
    logger = logs.new_logger(__app_name__, False)

    app_config = CoreConfigManager().get_config()
    http_client = HttpClient(logger)

    i18n = generate_i18n(app_config, resource.get_path('locale'))

    cache_factory = DefaultMemoryCacheFactory(expiration_time=0)

    context = ApplicationContext(i18n=i18n,
                                 http_client=http_client,
                                 download_icons=bool(app_config['download']['icons']),
                                 app_root_dir=ROOT_DIR,
                                 cache_factory=cache_factory,
                                 disk_loader_factory=DefaultDiskCacheLoaderFactory(logger),
                                 logger=logger,
                                 distro=util.get_distro(),
                                 file_downloader=AdaptableFileDownloader(logger, bool(app_config['download']['multithreaded']),
                                                                         i18n, http_client, app_config['download']['multithreaded_client']),
                                 app_name=__app_name__,
                                 internet_checker=InternetChecker(offline=False))

    managers = gems.load_managers(context=context, locale=i18n.current_key, config=app_config, default_locale=DEFAULT_I18N_KEY)

    cli = CLIManager(GenericSoftwareManager(managers, context=context, config=app_config))

    if args.command == 'updates':
        cli.list_updates(args.format)


if __name__ == '__main__':
    main()
