#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	Testing the simpleBlog main module
"""
import tornado.testing
from simpleBlog import simpleBlog

class test_routes (tornado.testing.AsyncHTTPTestCase):
	"""
		Test existence of methods on the / url
	"""
	def get_app(self):
		return simpleBlog.application
	
	def test_home_get (self):
		response = self.fetch('/', method="GET")
		self.assertNotEqual(response.code, 405)


	def test_home_post (self):
		response = self.fetch('/', method="POST", body="")
		self.assertEqual(response.code, 405)


	def test_home_put (self):
		response = self.fetch('/', method="PUT", body="")
		self.assertEqual(response.code, 405)


	def test_home_delete (self):
		response = self.fetch('/', method="DELETE")
		self.assertEqual(response.code, 405)
