#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	A simple blog application.
	The main goal of this application is to provide a blog engine that is as simple to use as possible.
"""

import tornado.ioloop
import tornado.web
import logging
from article import Article
from comment import Comment
from user import User


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Home (tornado.web.RequestHandler):
	def get(self):
		"""
			Display the home page
		"""
		raise NotImplementedError()


application = tornado.web.Application([
		(r"/", Home),					# /
		(r"/user/(.*)", User),			# /user/username_or_email
		(r"/(.*)(?=/)/(.*)", Comment), 	# /title_of_article/comment_id
		(r"/(.*)", Article),			# /title_of_article
	])


if __name__ == '__main__':
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()


