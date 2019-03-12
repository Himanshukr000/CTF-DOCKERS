#
# Authentication service model
#

import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = sqlalchemy.ext.declarative.declarative_base()
def setup_db(path=':memory:'):
	global Session

	engine = sqlalchemy.create_engine('sqlite:///' + path)
	Session = sessionmaker(bind=engine)
	Base.metadata.create_all(engine)

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	pass_salt = Column(String)
	pass_hash = Column(String)

class Tag(Base):
	__tablename__ = 'tags'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	key = Column(String)
	value = Column(String)

#
# HTTP interface to authentication service
#

import tornado.ioloop
import tornado.web

import hashlib
import base64
import json
import os

def jsonpack(x):
	return json.dumps(x, separators=(',',':'))

class ListHandler(tornado.web.RequestHandler):
	
	def get(self):
		session = Session()
		users = [user.name for user in session.query(User.name).all()]
		self.write(jsonpack(users))

class CreateUserHandler(tornado.web.RequestHandler):
	
	def post(self, username):
		session = Session()
		if session.query(User).filter_by(name=username).count():
			raise tornado.web.HTTPError(400)
		new_user = User(name=username, pass_salt='', pass_hash='')
		session.add(new_user)
		session.commit()

class DeleteUserHandler(tornado.web.RequestHandler):

	def post(self, username):
		session = Session()
		user = session.query(User).filter_by(name=username).first()
		if user is None:
			raise tornado.web.HTTPError(404)
		session.query(Tag).filter_by(user_id=user.id).delete()
		session.delete(user)
		session.commit()

class SetPasswordHandler(tornado.web.RequestHandler):
	
	def post(self, username):
		try:
			args = json.loads(self.request.body)
		except ValueError:
			raise tornado.web.HTTPError(400)
		session = Session()
		try:
			password = args['password'].encode('utf-8')
		except (TypeError, KeyError, UnicodeDecodeError):
			raise tornado.web.HTTPError(400)
		pass_salt = os.urandom(6)
		pass_hash = hashlib.md5(pass_salt + password).digest()
		user = session.query(User).filter_by(name=username).first()
		user.pass_salt = base64.b64encode(pass_salt)
		user.pass_hash = base64.b64encode(pass_hash)
		session.commit()

class CheckPasswordHandler(tornado.web.RequestHandler):
	
	def post(self, username):
		try:
			args = json.loads(self.request.body)
		except ValueError:
			raise tornado.web.HTTPError(400)
		session = Session()
		try:
			password = args['password'].encode('utf-8')
		except (TypeError, KeyError, UnicodeDecodeError):
			raise tornado.web.HTTPError(400)
		user = session.query(User).filter_by(name=username).first()
		if user is None:
			raise tornado.web.HTTPError(404)
		pass_salt = base64.b64decode(user.pass_salt)
		pass_hash = base64.b64decode(user.pass_hash)
		test_hash = hashlib.md5(pass_salt + password).digest()
		if pass_hash == test_hash:
			self.write(jsonpack(True))
		else:
			self.write(jsonpack(False))

class SetTagHandler(tornado.web.RequestHandler):

	def post(self, username):
		try:
			args = json.loads(self.request.body)
		except ValueError:
			raise tornado.web.HTTPError(400)
		session = Session()
		try:
			key = args['key']
			value = args['value'] 
		except (TypeError, KeyError):
			raise tornado.web.HTTPError(400)
		user = session.query(User).filter_by(name=username).first()
		if user is None:
			raise tornado.web.HTTPError(404)
		tag = session.query(Tag).filter_by(user_id=user.id, key=key).first()
		if tag is None:
			tag = Tag(user_id=user.id, key=key, value=value)
			session.add(tag)
		else:
			tag.value = value
		session.commit()

class DelTagHandler(tornado.web.RequestHandler):

	def post(self, username):
		try:
			args = json.loads(self.request.body)
		except ValueError:
			raise tornado.web.HTTPError(400)
		session = Session()
		try:
			key = args['key']
		except (TypeError, KeyError):
			raise tornado.web.HTTPError(400)
		user = session.query(User).filter_by(name=username).first()
		if user is None:
			raise tornado.web.HTTPError(404)
		session.query(Tag).filter_by(user_id=user.id, key=key).delete()
		session.commit()
	
class GetTagHandler(tornado.web.RequestHandler):
	
	def post(self, username):
		try:
			args = json.loads(self.request.body)
		except (TypeError, ValueError):
			raise Tornado.web.HTTPError(400)
		session = Session()
		try:
			key = args['key']
			default = args['default']
		except KeyError:
			raise tornado.web.HTTPError(400)
		user = session.query(User).filter_by(name=username).first()
		if user is None:
			raise tornado.web.HTTPError(404)
		tag = session.query(Tag).filter_by(user_id=user.id, key=key).first()
		if tag is None:
			self.write(default)
		else:
			self.write(tag.value)

def serve(port):
	application = tornado.web.Application([
		(r'/list', ListHandler),
		(r'/create_user/(.*)', CreateUserHandler),
		(r'/delete_user/(.*)', DeleteUserHandler),
		(r'/set_password/(.*)', SetPasswordHandler),
		(r'/check_password/(.*)', CheckPasswordHandler),
		(r'/set_tag/(.*)', SetTagHandler),
		(r'/del_tag/(.*)', DelTagHandler),
		(r'/get_tag/(.*)', GetTagHandler)
	])
	application.listen(port, address='127.0.0.1')
	tornado.ioloop.IOLoop.instance().start()

#
# Script interface
#

import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('port', type=int, default=6998)
	parser.add_argument('dbpath', type=str)
	args = parser.parse_args()
	setup_db(args.dbpath)
	serve(args.port)
