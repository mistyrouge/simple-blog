#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	Testing the simpleBlog.user module
"""
import tornado.testing
from simpleBlog import simpleBlog

class test_routes (tornado.testing.AsyncHTTPTestCase):
	"""
		Test existence of methods on the /user/ url
	"""
	def get_app(self):
		return simpleBlog.application
	
	def test_user_get (self):
		response = self.fetch('/user/', method="GET")
		self.assertNotEqual(response.code, 405)


	def test_user_post (self):
		response = self.fetch('/user/', method="POST", body="")
		self.assertNotEqual(response.code, 405)


	def test_user_put (self):
		response = self.fetch('/user/', method="PUT", body="")
		self.assertNotEqual(response.code, 405)


	def test_user_delete (self):
		response = self.fetch('/user/', method="DELETE")
		self.assertNotEqual(response.code, 405)
