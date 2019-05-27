#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'c0de'
SITENAME = "c0de's ongoing development"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Personal Site', 'https://c0defox.es'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/alopexc0de'),
          ('Keybase', 'https://keybase.io/alopexc0de'),
          ('Telegram', 'https://t.me/c0defox'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True  # Use directories in content to specify the category
DEFAULT_CATEGORY = 'none'

PLUGINS = ['encrypt_content']

ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted and requires a password to unlock'
}
