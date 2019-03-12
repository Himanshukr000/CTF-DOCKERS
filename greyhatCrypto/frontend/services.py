import time
import json

import tornado.httpclient

http_client = tornado.httpclient.HTTPClient()

class HTTPServiceProxy(object):

    def __init__(self, host='localhost', port=6999, cache_timeout=5.0):
        self._host = host
        self._port = port
        self._cache_timeout = cache_timeout

        self._cache = {}
        self._cache_time = {}

    def get(self, *path):
        print 'http://%s:%d/%s' % (self._host, self._port, '/'.join(path))
        if path in self._cache and \
            self._cache_time[path] + self._cache_timeout > time.time():
            return self._cache[path]

        try:
            response = http_client.fetch('http://%s:%d/%s' % (self._host, self._port, '/'.join(path)))
            self._cache[path] = response.body
            self._cache_time[path] = time.time()
            return response.body
        except tornado.httpclient.HTTPError as e:
            if path in self._cache:
                del self._cache[path]
            return None

    def post(self, *path, **kwargs):
        url = 'http://%s:%d/%s' % (self._host, self._port, '/'.join(path))
        print url
        try:
            request = tornado.httpclient.HTTPRequest(url, method='POST', body=json.dumps(kwargs))
            response = http_client.fetch(request)
            return response.body
        except tornado.httpclient.HTTPError as e:
            return None

class MonitorProxy(HTTPServiceProxy):
    """
    Proxy object for the challenge monitor service.
    """

    def __init__(self):
        super(MonitorProxy, self).__init__(host='localhost', port=6999, cache_timeout=0.0)
        
    @property
    def challenges(self):
        return json.loads(self.get('list'))
    
    @property
    def visible_challenges(self):
        return json.loads(self.get('list_visible'))

    def status(self, challenge):
        try:
            return json.loads(self.get('status')).get(challenge, None)
        except TypeError:
            return None

    def show(self, challenge):
        self.post('show', challenge)

    def hide(self, challenge):
        self.post('hide', challenge)

    def start(self, challenge):
        self.post('start', challenge)

    def stop(self, challenge):
        self.post('stop', challenge)

    def metadata(self, challenge):
        try:
            return json.loads(self.get('metadata', challenge))
        except TypeError:
            return None

    def fetch_file(self, challenge, filename):
        return self.get('static_files', challenge, filename)

monitor = MonitorProxy()

class AuthProxy(HTTPServiceProxy):
    """
    Proxy object for the user authentication serivce.
    """

    def __init__(self, host='127.0.0.1', port=6998, cache_timeout=1.0):
        super(AuthProxy, self).__init__(host='localhost', port=6998, cache_timeout=1.0)

    @property
    def users(self):
        return json.loads(self.get('list'))

    def create_user(self, user):
        self.post('create_user', user)

    def is_admin(self, user):
        try:
            return json.loads(self.post('get_tag', user, key='is_admin', default='false'))
        except (ValueError, TypeError):
            return False

    def is_playing(self, user):
        try:
            return json.loads(self.post('get_tag', user, key='is_playing', default='true'))
        except (ValueError, TypeError):
            return False

    def set_password(self, user, password):
        self.post('set_password', user, password=password)

    def check_password(self, user, password):
        try:
            return json.loads(self.post('check_password', user, password=password))
        except TypeError:
            return False

    def set_tag(self, user, key, value):
        self.post('set_tag', user, key=key, value=json.dumps(value))

    def get_tag(self, user, key, default=''):
        return self.post('get_tag', user, key=key, default=default)

auth = AuthProxy()

class ScoreboardProxy(HTTPServiceProxy):
    """
    Proxy object for the scoreboard service.
    """

    def __init__(self, host='127.0.0.1', port=6997, cache_timeout=1.0):
        super(ScoreboardProxy, self).__init__(host='localhost', port=6997, cache_timeout=1.0)

    def capture(self, user, challenge):
        self.post('capture', challenge, user=user)

    def get_captures_by_user(self, user):
        return json.loads(self.get('get_captures_by_user', user))

    def get_captures_by_challenge(self, challenge):
        return json.loads(self.get('get_captures_by_challenge', challenge))
    
scoreboard = ScoreboardProxy()
