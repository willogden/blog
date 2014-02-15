#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Will Ogden'
SITENAME = u'willo.gd/en'
SITESUBTITLE = u'Web Developer, Father, Cliché'
SITEURL = '/en'
GITHUB_URL = 'http://github.com/willogden/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/will_ogden'),
          ('github', 'http://github.com/willogden'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH = 'content/'
OUTPUT_PATH = 'en/'
THEME = "themes/pure"

MENUITEMS = [('Home','/en')]
GOOGLE_ANALYTICS = "UA-41253807-2"
DISQUS_SITENAME = "willogden1"
