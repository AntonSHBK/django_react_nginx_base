# -*- coding: utf-8 -*-
import os

DEBUG = int(os.environ.get("DEBUG", default=False))

if DEBUG:
    from .dev_settings import *
else:
    from .prod_settings import *