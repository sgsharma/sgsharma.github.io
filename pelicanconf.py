#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sasha Sharma'
SITENAME = 'themightycomma'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

THEME = 'attila'
STATIC_PATHS = ['images']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True