#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sgsharma'
SITENAME = u'themightycomma'
SITESUBTITLE = u''
SITEURL = ''

PATH = 'content'

# DEFAULT_DATE = 'fs'
# DEFAULT_DATE_FORMAT = '%d %b %Y'
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
# FEED_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
# FEED_RSS = 'feed/index.html'
# FEED_ATOM = 'feed/atom/index.html'
# FEED_ALL_RSS = None
# FEED_ALL_ATOM = None
# TRANSLATION_FEED_RSS = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# TAG_FEED_RSS = 'tag/{slug}/feed/index.html'
# TAG_FEED_ATOM = 'tag/{slug}/feed/atom/index.html'

# http://example.com/category/categoryname/feed
CATEGORY_FEED_RSS = 'category/{slug}/feed/index.html'
CATEGORY_FEED_ATOM = 'category/{slug}/feed/atom/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (
          ('Twitter', 'http://twitter.com/themightycomma'),
          )

DEFAULT_PAGINATION = 3

STATIC_PATHS = ['images']

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
# CATEGORY_URL = 'category/{slug}'
# CATEGORY_SAVE_AS = 'category/{slug}/index.html'
# CATEGORIES_SAVE_AS = 'catgegories.html'
# TAG_URL = 'tag/{slug}'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
# TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

THEME = 'attila'

### Theme specific settings

COLOR_SCHEME_CSS = 'monokai.css'

# To set background image for the home page.
HOME_COVER = 'images/cover.jpg'

AUTHORS_BIO = {
  "sgsharma": {
    "name": "Sasha",
    "cover": "images/sgsharma.png",
    "image": "images/cover.jpg",
    "website": "https://sgsharma.github.io",
    "location": "San Francisco",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True