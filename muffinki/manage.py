#!/usr/bin/env python

import os
from django.core.management import execute_manager


DEFAULT_SETTING_MODULE = 'settings.defaults'


def import_settings():
    """Return django settings module object

    Import settings using path from DJANGO_SETTINGS_MODULE shell environment
    variable or if does not exists, use DEFAULT_SETTING_MODULE
    """
    settings_mod = os.environ.get('DJANGO_SETTINGS_MODULE',
            DEFAULT_SETTING_MODULE)
    if settings_mod:
        mod_parts = settings_mod.split('.')
        settings = __import__(settings_mod, globals(), locals(), mod_parts, -1)
        return settings

    #this should never happen!
    raise ImportError("Django settting import error")


if __name__ == "__main__":
    execute_manager(import_settings())