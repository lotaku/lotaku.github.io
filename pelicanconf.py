#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lotaku'
SITENAME = u'Lotaku'
SITEURL = 'http://lotaku.github.io'
# 如果要在本地调试测试显示disqus,修改SITEURL
# SITEURL = 'http://127.0.0.1:8000'
DISQUS_SITENAME = u'lotaku'

GITHUB_URL = 'http://github.com/ametaireau/'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['/Users/l/learnspace/pelican-plugins']
PLUGINS = ['tipue_search', 'i18n_subsites']
# THEME = '/Users/l/learnspace/pelican-themes-master/pelican-bootstrap3'
THEME = '/Users/l/learnspace/blog/themes_self/pelican-elegant-1.3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search', 'tags')

STATIC_PATHS = [
    # 'pictures',
    # 'extra/robots.txt',
    'static',
    'extra/CNAME',
]

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
# YEAR_ARCHIVE_SAVE_AS = ''
# MONTH_ARCHIVE_SAVE_AS = ''
# DAY_ARCHIVE_SAVE_AS = ''

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
