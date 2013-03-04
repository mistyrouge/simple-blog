#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	Testing the simpleBlog.comment module
"""
import tornado.testing
from simpleBlog import simpleBlog

class test_routes (tornado.testing.AsyncHTTPTestCase):
	"""
		Test existence of methods on the /…/comment_id url
	"""
	def get_app(self):
		return simpleBlog.application
	
	
	def test_comment_get (self):
		response = self.fetch("/some_article/", method="GET")
		self.assertEqual(response.code, 405)


	def test_comment_post (self):
		response = self.fetch('/some_article/', method="POST", body="")
		self.assertNotEqual(response.code, 405)


	def test_comment_put (self):
		response = self.fetch('/some_article/', method="PUT", body="")
		self.assertNotEqual(response.code, 405)


	def test_comment_delete (self):
		response = self.fetch('/some_article/', method="DELETE")
		self.assertNotEqual(response.code, 405)
