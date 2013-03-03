#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class User (tornado.web.RequestHandler):
	def get(self, assertion):
		"""
			Login a user and return it's information
		"""
		log.warn("assertion : {}".format(assertion))
		raise NotImplementedError()


	def post(self, username):
		"""
			Modify a user's information
		"""
		raise NotImplementedError()


	def put(self, username): 
		"""
			Create a new user.
			We need at least one email address
		"""
		raise NotImplementedError()


	def delete(self, username): 
		"""
			Delete a user
		"""
		raise NotImplementedError()



