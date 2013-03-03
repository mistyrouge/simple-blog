#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Comment (tornado.web.RequestHandler):
	def post(self, article_title, comment_id):
		"""
			Modify a comment
		"""
		raise NotImplementedError()


	def put(self, article_title, comment_id):
		"""
			Create a new comment
		"""
		raise NotImplementedError()


	def delete(self, article_title, comment_id):
		"""
			Delete a comment
		"""
		raise NotImplementedError()



