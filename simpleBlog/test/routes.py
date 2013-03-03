#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	Test that all routes have been implemented
"""

import tornado.testing
import simpleBlog

class Routes (tornado.testing.AsyncHTTPTestCase):
	def get_app(self):
		return simpleBlog.application
	
	def test_home (self):
		"""
			Check that the home page exists
		"""
		response = self.fetch('/')
		self.assertEqual(response.code, 200)
		
