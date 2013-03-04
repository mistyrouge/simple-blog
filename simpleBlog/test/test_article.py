#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	Testing the simpleBlog.article module
"""
import tornado.testing
from simpleBlog import simpleBlog

class test_routes (tornado.testing.AsyncHTTPTestCase):
	"""
		Test existence of methods on the /title_of_article url
	"""
	def get_app(self):
		return simpleBlog.application
	
	
	def test_article_get (self):
		response = self.fetch("/some_article", method="GET")
		self.assertNotEqual(response.code, 405)


	def test_article_post (self):
		response = self.fetch('/some_article', method="POST", body="")
		self.assertNotEqual(response.code, 405)


	def test_article_put (self):
		response = self.fetch('/some_article', method="PUT", body="")
		self.assertNotEqual(response.code, 405)


	def test_article_delete (self):
		response = self.fetch('/some_article', method="DELETE")
		self.assertNotEqual(response.code, 405)
