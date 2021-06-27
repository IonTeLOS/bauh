import os

import urllib3

from wasf import ROOT_DIR
from wasf.api.abstract.context import ApplicationContext
from wasf.api.http import HttpClient
from wasf.cli import __app_name__, cli_args
from wasf.cli.controller import CLIManager
from wasf.commons.internet import InternetChecker
from wasf.context import generate_i18n, DEFAULT_I18N_KEY
from wasf.view.core import gems
from wasf.view.core.config import CoreConfigManager
from wasf.view.core.controller import GenericSoftwareManager
from wasf.view.core.downloader import AdaptableFileDownloader
from wasf.view.util import logs, util, resource
from wasf.view.util.cache import DefaultMemoryCacheFactory
from wasf.view.util.disk import DefaultDiskCacheLoaderFactory


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
