#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'c0de'
SITENAME = "c0de's development"
SITESUBTITLE = "<i class=\"far fa-dollar-sign\"></i> cat /proc/c0de/thoughts"
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
#LINKS = (('Personal Site', 'https://c0defox.es'),)

# Social widget
SOCIAL = (('github', 'https://github.com/alopexc0de'),
          ('keybase', 'https://keybase.io/alopexc0de'),
          ('telegram', 'https://t.me/c0defox'),)

SHARE = True

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True  # Use directories in content to specify the category
DEFAULT_CATEGORY = 'none'

# Theme settings

THEME = "theme"
THEME_STATIC_PATHS = ['static']
CSS_FILE = "main.css"

# Required settings to allow correct behavior of theme
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'past_readings', 'search', 'tipue_search')

FOOTER = ("Content produced is &copy; <a href=\"mailto:c0de@c0de.dev\">c0de</a>. All rights reserved.<br />" +
          "Code snippets on this site are, unless otherwise noted, released under " +
          "<a href=\"https://opensource.org/licenses/MIT\" target=\"_license\">The MIT License</a>.")

TWITTER_USERNAME = "foxyc0de"
DISPLAY_PAGES_ON_MENU = False

# Plugin paths and activated ones

PLUGIN_PATHS = ['plugins/encrypt-content',
                'plugins/upstream',
                'plugins']

PLUGINS = ['encrypt_content', 'deadlinks', 'bootstrapify', 'tipue_search']

# Plugin specific settings below

# Encrypt-Content Settings
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted and requires a password to unlock'
}

# Deadlink Settings
DEADLINK_VALIDATION = True

DEADLINK_OPTS = {
    'archive': True,
    'classes': ['disabled'],
    'labels': True,
    'timeout_duration_ms': 3000,
    'timeout_is_error': False
}
