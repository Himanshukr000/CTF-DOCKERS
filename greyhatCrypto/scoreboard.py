#
# Scoreboard service model
#

import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

Base = sqlalchemy.ext.declarative.declarative_base()
def setup_db(path=':memory:'):
    global Session

    engine = sqlalchemy.create_engine('sqlite:///' + path)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

class Capture(Base):
    __tablename__ = 'captures'

    id = Column(Integer, primary_key=True)
    user = Column(String)
    challenge = Column(String)
    timestamp = Column(Float)

#
# HTTP interface to scoreboard service
#

import tornado.ioloop
import tornado.web

import hashlib
import base64
import time
import json
import os

def jsonpack(x):
    return json.dumps(x, separators=(',',':'))

class CaptureHandler(tornado.web.RequestHandler):

    def post(self, challenge):
        try:
            args = json.loads(self.request.body)
        except ValueError:
            raise tornado.web.HTTPError(400)
        session = Session()
        try:
            user = args['user']
        except (TypeError, KeyError):
            raise tornado.web.HTTPError(400)

        print challenge, user

        capture = session.query(Capture).filter_by(user=user, challenge=challenge).first()
        if capture is None:
            capture = Capture(user=user, challenge=challenge, timestamp=time.time())
            session.add(capture)
            session.commit()

class GetCapturesByChallengeHandler(tornado.web.RequestHandler):

    def get(self, challenge):
        session = Session()
        captures = [(c.user, c.timestamp) for c in session.query(Capture).filter_by(challenge=challenge).all()]
        self.write(jsonpack(captures))

class GetCapturesByUserHandler(tornado.web.RequestHandler):

    def get(self, user):
        session = Session()
        captures = [(c.challenge, c.timestamp) for c in session.query(Capture).filter_by(user=user).all()]
        self.write(jsonpack(captures))

def serve(port):
    application = tornado.web.Application([
        (r'/capture/(.*)', CaptureHandler),
        (r'/get_captures_by_user/(.*)', GetCapturesByUserHandler),
        (r'/get_captures_by_challenge/(.*)', GetCapturesByChallengeHandler)
    ])
    application.listen(port, address='127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()

#
# Script interface
#

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, default=6997)
    parser.add_argument('dbpath', type=str)
    args = parser.parse_args()
    setup_db(args.dbpath)
    serve(args.port)
