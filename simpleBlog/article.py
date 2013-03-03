#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Article (tornado.web.RequestHandler):
	def get(self, title):
		"""
			Display an article
		"""
		raise NotImplementedError()
		
	
	def post(self, title):
		"""
			Modify an article
		"""
		raise NotImplementedError()
		
	
	def put(self, title):
		"""
			Create an article
		"""
		raise NotImplementedError()



