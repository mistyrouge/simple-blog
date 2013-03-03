#!/usr/bin/env python
#-*- coding:utf-8 -*-

from distutils.core import setup

setup(
	name="simpleBlog",
	packages= ["simpleBlog"],
	version=0.1,
	author="Dorian JAMINAIS",
	author_email="dorian@jaminais.fr",
	url="http://github.com/mistyrouge/simple-blog",
	description="A simple blogging application.",
	long_description="""simpleBlog tries to simplify the blogging experience.
No need to understand how a blog works to use simple blog. Just install it, tell it your email address and you're good to go. THere is no special administrative area. If you want to add a new article, just write it from your home page. Want to fix a typo in your text ? just correct it while reading it.""",
	classifiers=[
		"Programming Language :: Python",
		"Framework :: tornado",
		"Operating System :: OS Independent",
		"Intended Audience :: End Users",
		"Topic :: Internet :: Blog"
	]
)
