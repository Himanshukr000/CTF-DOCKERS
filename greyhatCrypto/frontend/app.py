import os
import json
import os.path
import datetime

import tornado.web
import tornado.ioloop
import tornado.template

from services import monitor, auth, scoreboard

#
# Base RequestHandler with utility methods
#

class RequestHandler(tornado.web.RequestHandler):
    
    @property
    def user(self):
        return self.get_secure_cookie('user')

    @user.setter
    def user(self, user):
        if user is None:
            self.clear_cookie('user')
        else:
            self.set_secure_cookie('user', user)

    @property
    def is_admin(self):
        username = self.get_secure_cookie('user')
        if not username:
            return False
        else:
            return auth.is_admin(username)

    @property
    def is_playing(self):
        username = self.get_secure_cookie('user')
        if not username:
            return False
        else:
            return auth.is_playing(username)

template_loader = tornado.template.Loader('templates/')

#
# Main page
#

class IndexHandler(RequestHandler):

    def get(self):
        self.redirect('/scoreboard')

#
# Challenge presentation and management
#

class ChallengeIndexHandler(RequestHandler):

    def get(self):
        if self.is_admin:
            challenge_list = monitor.challenges
        else:
            challenge_list = monitor.visible_challenges

        metadata = { name : monitor.metadata(name) for name in challenge_list }
        challenge_list = sorted(challenge_list, key=lambda n: (metadata[n]['points'], n))

        challenges = [
            {
                'name' : name,
                'points' : metadata[name]['points'],
                'captures' : len(scoreboard.get_captures_by_challenge(name)),
                'status' : make_status_widget(self, monitor.status(name), metadata[name])
            }
            for name in challenge_list
        ]

        self.render('templates/challenge_index.html',
            user=self.user,
            selected='challenges',
            challenges=challenges
        )

def make_status_widget(self, status, metadata, button=False):

    if not button:
        if status['running']:
            status_widget = """<div class="box green">Running on %s port %d</div>
            """ % (status['port'][0].upper(), status['port'][1])
        elif 'run_type' not in metadata:
            status_widget = """<div class="box green">Static files only</div>"""
        else:
            status_widget = """<div class="box red">Down for maintainance</div>"""
    else:
        if status['visible']:
            if status['running']:
                status_widget = """
                <div class="box green">
                  Running on %s port %d
                  <form method="post">
                    <input type="hidden" name="action" value="stop">
                    <input type="submit" value="Stop" class="submit">
                  </form>
                </div>
                """ % (status['port'][0].upper(), status['port'][1])
            elif 'run_type' not in metadata:
                status_widget = """
                <div class="box green">
                  Static files only
                  <form method="post">
                    <input type="hidden" name="action" value="hide">
                    <input type="submit" value="Hide" class="submit">
                  </form>
                </div>
                """
            else:
                status_widget = """
                <div class="box red">
                  Down for maintainance
                  <form method="post">
                    <input type="hidden" name="action" value="start">
                    <input type="submit" value="Start" class="submit">
                  </form>
                  <form method="post">
                    <input type="hidden" name="action" value="hide">
                    <input type="submit" value="Hide" class="submit">
                  </form>
                </div>
                """
        else:
            status_widget = """
            <div class="box purple">
              Hidden
              <form method="post">
                <input type="hidden" name="action" value="show">
                <input type="submit" value="Show" class="submit">
              </form>
            </div>
            """
    return status_widget

class ChallengePageHandler(RequestHandler):

    def get(self, challenge):
        status = monitor.status(challenge)
        metadata = monitor.metadata(challenge)
        if status == None or metadata == None:
            raise tornado.web.HTTPError(404)

        if not self.is_admin and not status['visible']:
            raise tornado.web.HTTPError(404)

        status_widget = make_status_widget(self, status, metadata, self.is_admin)

        self.render('templates/challenge.html',
            user=self.user,
            selected='challenges',
            challenge_files=metadata.get('public_files', []),
            challenge_name=metadata.get('name', challenge),
            challenge_author=metadata.get('author', 'Anonymous'),
            challenge_points=metadata.get('points', 0),
            challenge_solves=len(scoreboard.get_captures_by_challenge(challenge)),
            challenge_description=metadata.get('description', ''),
            show_capture=auth.is_playing(self.user or ''),
            status=status_widget,
        )

    def post(self, challenge):
        action = self.get_argument('action', None)
        if action == 'capture':
            self.action_capture(challenge, self.get_argument('flag'))
        elif action == 'start':
            self.action_start(challenge)
        elif action == 'stop':
            self.action_stop(challenge)
        elif action == 'show':
            self.action_show(challenge)
        elif action == 'hide':
            self.action_hide(challenge)
        else:
            raise tornado.web.HTTPError(400)
        self.redirect('')

    def action_capture(self, challenge, flag):
        if not self.is_playing:
            raise tornado.web.HTTPError(403)
        
        status = monitor.status(challenge)
        metadata = monitor.metadata(challenge)
        if status == None or metadata == None or not status['visible']:
            raise tornado.web.HTTPError(403)

        if metadata['flag'].strip() == flag.strip():
            scoreboard.capture(self.user, challenge)
            scoreboard_cache.dirty = True

    def action_start(self, challenge):
        if not self.is_admin:
            raise tornado.web.HTTPError(403)
        monitor.start(challenge)

    def action_stop(self, challenge):
        if not self.is_admin:
            raise tornado.web.HTTPError(403)
        monitor.stop(challenge)

    def action_show(self, challenge):
        if not self.is_admin:
            raise tornado.web.HTTPError(403)
        monitor.show(challenge)

    def action_hide(self, challenge):
        if not self.is_admin:
            raise tornado.web.HTTPError(403)
        monitor.hide(challenge)

class ChallengeFilesHandler(RequestHandler):

    def get(self, challenge, filename):
        self.set_header('Content-Type', 'application/octet-stream')
        self.write(monitor.fetch_file(challenge, filename))

#
# Scoreboard
#

class ScoreboardCache(object):
    """
    Entries are tuples (username, score, captures, last_capture_timestamp)
    """

    def __init__(self):
        self.dirty = True
        self.update()

    def update(self):
        if not self.dirty:
            return
        self._update()

    def _update(self):
        self.dirty = False

        challenge_points = { 
            challenge : monitor.metadata(challenge)['points']
            for challenge in monitor.challenges
        }

        entries = []

        for user in auth.users:
            if not auth.is_playing(user):
                continue

            user_points = 0
            user_captures = 0
            user_last_capture_timestamp = float('-inf')
            for challenge, timestamp in scoreboard.get_captures_by_user(user):
                user_captures += 1
                user_points += challenge_points[challenge]
                if user_last_capture_timestamp < float(timestamp):
                    user_last_capture_timestamp = float(timestamp)

            entries.append((user, user_points, user_captures, user_last_capture_timestamp))
        
        self.scoreboard_list = sorted(entries, key=lambda e: (e[1], -e[3]), reverse=True)

scoreboard_cache = ScoreboardCache()

class ScoreboardHandler(RequestHandler):

    def get(self):
        self.render('templates/scoreboard.html',
            user=self.user,
            selected='scoreboard',
            scoreboard=[
                {
                    'user': entry[0],
                    'score': entry[1],
                    'captures': entry[2],
                    'last_time': datetime.datetime.fromtimestamp(entry[3]).isoformat().replace('T', ' ')
                        if entry[3] != float('-inf') else 'N/A'
                }
                for entry in scoreboard_cache.scoreboard_list
            ]
        )

#
# Users and authentication
#

class UserLoginHandler(RequestHandler):
    
    def get(self):
        if self.user is not None:
            self.redirect('/scoreboard')
            return
        self.render('templates/login.html',
            user=None,
            selected=None,
            error=None
        )
    
    def post(self):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        
        if auth.check_password(username, password):
            self.user = username
            self.redirect('/login')
        else:
            self.render('templates/login.html',
                user=None,
                selected=None,
                error='login failed'
            )

class UserLogoutHandler(RequestHandler):
    
    def post(self):
        self.user = None
        self.redirect('/scoreboard')

class UserCreateHandler(RequestHandler):

    def get(self):
        self.render('templates/create_user.html',
            user=None,
            selected=None,
            error=None
        )
    
    def post(self):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        email = self.get_body_argument('email')
        shirtsize = self.get_body_argument('shirtsize')

        if username in auth.users:
            self.render('templates/create_user.html',
                user=None,
                selected=None,
                error='user exists'
            )
            return

        auth.create_user(username)
        auth.set_password(username, password)
        auth.set_tag(username, 'email', email)
        auth.set_tag(username, 'shirtsize', shirtsize)
        self.user = username
        
        scoreboard_cache.dirty = True

        self.redirect('/scoreboard')

if __name__ == '__main__':
    if not os.path.isfile('../var/cookie.secret'):
        with open('../var/cookie.secret', 'w') as cookie_secret_file:
            cookie_secret = os.urandom(16)
            cookie_secret_file.write(cookie_secret)
    else:
        cookie_secret = ''.join(open('../var/cookie.secret'))

    app = tornado.web.Application(
        [
            (r'/', IndexHandler),
            (r'/challenges/?', ChallengeIndexHandler),
            (r'/challenges/([A-Za-z0-9_-]+)', ChallengePageHandler),
            (r'/challenges/([A0Za-z0-9_-]+)/(.*)', ChallengeFilesHandler),
            (r'/scoreboard/?', ScoreboardHandler),
            (r'/login', UserLoginHandler),
            (r'/logout', UserLogoutHandler),
            (r'/create_user', UserCreateHandler)
        ],
        static_path='static',
        cookie_secret=cookie_secret
    )
    app.listen(8080)
    tornado.ioloop.PeriodicCallback(scoreboard_cache.update, 2000).start()
    tornado.ioloop.PeriodicCallback(scoreboard_cache._update, 1800000).start()
    tornado.ioloop.IOLoop.instance().start()
