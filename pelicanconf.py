#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'

AUTHOR = 'Gints Murāns'
SITENAME = 'Dzīvoklis'
SITEURL = ''

TIMEZONE = 'Europe/Riga'
DEFAULT_LANG = 'lv'

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 180

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/gintsmurans'),
    ('instagram', 'https://www.instagram.com/gintsmurans/', 'instagram'),
    ('github', 'http://github.com/gintsmurans')
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME stuff
THEME = 'theme'
BOOTSTRAP_THEME = 'united'

DISPLAY_CATEGORIES_ON_MENU = False
PYGMENTS_STYLE = 'solarizeddark'
DISPLAY_BREADCRUMBS = False
FAVICON = ''
DISPLAY_ARTICLE_INFO_ON_INDEX = False

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5

DISQUS_NO_ID = True
CC_LICENSE = 'CC-BY'
