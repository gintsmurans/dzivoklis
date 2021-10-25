#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'
OUTPUT_PATH = '../output'

AUTHOR = 'Gints Murāns'
SITENAME = 'GM'
SITEURL = ''

TIMEZONE = 'Europe/Riga'
DEFAULT_LANG = 'lv'
LOCALE = 'lv_LV.UTF-8'

I18N_SUBSITES = {
    'en': {
        'SITENAME': 'GM',
        'AUTHOR': 'Gints Murāns',
        'LOCALE': 'en_US.UTF-8',
        'STATIC_PATHS': ['images', 'extra/favicon.png'],
        'LINKS': (
            ('4Apps', 'https://4apps.lv/products'),
        ),
    }
}

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 180

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.png': {'path': 'favicon.png'}
}

# Blogroll
LINKS = (
    ('Laacz ceļ māju', 'https://laacz.lv/category/celam-maju/'),
    ('Ģimenes māja', 'https://gimenesmaja.wordpress.com/'),
    ('Ģimenes māja 2', 'http://gimenesmaja.blogspot.com/'),
    ('Vasarnīca', 'http://vasarnica.blogspot.com/'),
    ('Koka māja', 'https://kokamaja.wordpress.com/'),
    ('Būvejot māju', 'https://buvejotmaju.wordpress.com/'),
    ('Ķiršu parks', 'https://kirsuparks.wordpress.com/'),
    ('Praktisko padomu bibliotēka', 'http://www.uzbuve.lv/'),
    ('Ko darītu savādāk', 'http://calis.delfi.lv/forums/(tema/4014436-ko-dzivokli-un-maja-taisitu-savadak/)/'),
    ('Varu pats', 'http://www.varupats.lv/'),
    ('Grīdas meistars', 'http://gridasmeistars.lv/')
)

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/gintsmurans'),
    ('instagram', 'https://www.instagram.com/gintsmurans/', 'instagram'),
    ('github', 'http://github.com/gintsmurans'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME stuff
THEME = 'theme'
BOOTSTRAP_THEME = 'united'

DISPLAY_CATEGORIES_ON_MENU = False
PYGMENTS_STYLE = 'solarizeddark'
DISPLAY_BREADCRUMBS = False
FAVICON = 'favicon.png'
DISPLAY_ARTICLE_INFO_ON_INDEX = False

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5

DISQUS_NO_ID = True
CC_LICENSE = 'CC-BY'
