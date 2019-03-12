#
# This is the challenge monitor daemon.
#

import subprocess
import random
import json
import os

from challengeutils import get_logfile, get_metadata, get_config
from challengeutils import is_challenge, challenge_list

visible_challenges = set()
challenge_processes = {}
challenge_port = {}

tcp_servers = { port : None for port in xrange(7000, 7500) }
udp_servers = { port : None for port in xrange(7500, 8000) }

def allocate_tcp_port(name, port=None):
    if port is None:
        ports = tcp_servers.keys()
        random.shuffle(ports)
        for port in ports:
            if tcp_servers[port] == None:
                tcp_servers[port] = name
                challenge_port[name] = ('tcp', port)
                return port
    else:
        if tcp_servers.get(port, True) is None:
            tcp_servers[port] = name
            challenge_port[name] = ('tcp', port)
            return port

def allocate_udp_port(name, port=None):
    if port is None:
        ports = udp_servers.keys()
        random.shuffle(ports)
        for port in ports:
            if udp_servers[port] == None:
                udp_servers[port] = name
                challenge_port[name] = ('udp', port)
                return port
    else:
        if udp_servers.get(port, True) is None:
            udp_servers[port] = name
            challenge_port[name] = ('udp', port)
            return port

def free_tcp_ports(name):
    for port in list(tcp_servers.keys()):
        if tcp_servers[port] == name:
            tcp_servers[port] = None
    if name in challenge_port:
        del challenge_port[name]

def free_udp_ports(name):
    for port in list(udp_servers.keys()):
        if udp_servers[port] == name:
            udp_servers[port] = None
    if name in challenge_port:
        del challenge_port[name]

def show_challenge(name):
    visible_challenges.add(name)

def hide_challenge(name):
    if name in visible_challenges:
        visible_challenges.remove(name)

def activate_challenge(name, config):
    metadata = get_metadata(name)
    
    if name in challenge_processes:
        return

    if 'run_type' in metadata:
        if metadata['run_type'] == 'tcpserver':
            config['port'] = allocate_tcp_port(name, config.get('port', None))
            config['host'] = '0.0.0.0'
        elif metadata['run_type'] == 'udpserver':
            config['port'] = allocate_udp_port(name, config.get('port', None))
            config['host'] = '0.0.0.0'

        if 'run_command' in metadata:
            logfile = get_logfile(name)
            old_cwd = os.getcwd()
            os.chdir('challenges/%s/' % name)
            challenge_processes[name] = subprocess.Popen(metadata['run_command'] % config,
                shell=True, stdin=None, stdout=logfile, stderr=logfile)
            os.chdir(old_cwd)

def deactivate_challenge(name):
    metadata = get_metadata(name)

    if 'run_type' in metadata:
        if metadata['run_type'] == 'tcpserver':
            free_tcp_ports(name)
        elif metadata['run_type'] == 'udpserver':
            free_udp_ports(name)

    if name in challenge_processes:
        if challenge_processes[name].poll() == None:
            challenge_processes[name].terminate()
        del challenge_processes[name]

def is_visible(name):
    return name in visible_challenges

def is_active(name):
    if name in challenge_processes:
        return challenge_processes[name].poll() == None
    return False

def gc():
    for name in list(challenge_processes.keys()):
        if challenge_processes[name].poll() != None:
            deactivate_challenge(name)

#
# HTTP interface to monitor
#

import tornado.ioloop
import tornado.web

def jsonpack(x):
    return json.dumps(x, separators=(',',':'))

class ListHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(jsonpack(challenge_list()))

class ListVisibleHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(jsonpack(sorted(visible_challenges)))

class ConfigHandler(tornado.web.RequestHandler):
    
    def get(self, name):
        if not is_challenge(name):
            raise tornado.web.HTTPError(404)
        self.write(jsonpack(get_config(name)))

class ShowHandler(tornado.web.RequestHandler):
    
    def post(self, name):
        print 'show', name
        if not is_challenge(name):
            raise tornado.web.HTTPError(404)
        show_challenge(name)

class HideHandler(tornado.web.RequestHandler):

    def post(self, name):
        print 'hide', name
        if not is_challenge(name):
            raise tornado.web.HTTPError(404)
        hide_challenge(name)

class StartHandler(tornado.web.RequestHandler):
    
    def post(self, name):
        print 'start', name
        if not is_challenge(name):
            raise tornado.web.HTTPError(404)
        activate_challenge(name, get_config(name))

class StopHandler(tornado.web.RequestHandler):
    
    def post(self, name):
        print 'stop', name
        if not is_challenge(name):
            raise tornado.web.HTTPError(404)
        deactivate_challenge(name)

class MetadataHandler(tornado.web.RequestHandler):
    
    def get(self, name):
        if not is_challenge(name):
            raise tornado.web.HTTPError(404)
        self.write(jsonpack(get_metadata(name)))

class StatusHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.write(jsonpack({
            name : {
                'visible' : is_visible(name),
                'running' : is_active(name),
                'port' : challenge_port.get(name, None)
            }
            for name in challenge_list()
        }))

class StaticFilesHandler(tornado.web.RequestHandler):

    def get(self, name, filename):
        if not is_challenge(name):
            raise tornado.web.HTTPError(404)

        metadata = get_metadata(name)
        if filename not in metadata['public_files']:
            raise tornado.web.HTTPError(404)
            
        file = open(os.path.join(os.getcwd(), 'challenges/%s/%s' % (name, filename)))
        for line in file:
            self.write(line)

def serve(port):
    application = tornado.web.Application([
        (r'/list', ListHandler),
        (r'/list_visible', ListVisibleHandler),
        (r'/config/(.*)', ConfigHandler),
        (r'/show/(.*)', ShowHandler),
        (r'/hide/(.*)', HideHandler),
        (r'/start/(.*)', StartHandler),
        (r'/stop/(.*)', StopHandler),
        (r'/metadata/(.*)', MetadataHandler),
        (r'/status', StatusHandler),
        (r'/static_files/([A-Za-z0-9_-]+)/(.*)', StaticFilesHandler)
    ])
    application.listen(port, address='127.0.0.1')
    
    gc_callback = tornado.ioloop.PeriodicCallback(gc, 1000)
    gc_callback.start()

    tornado.ioloop.IOLoop.instance().start()

#
# Script interface
#

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, default=6999)

    args = parser.parse_args()

    serve(args.port)
