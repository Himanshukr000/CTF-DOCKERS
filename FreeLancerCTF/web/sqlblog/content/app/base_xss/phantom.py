import signal
import time
import urlparse
from selenium import webdriver

class Spooky(object):
    driver = None
    def __init__(self):
        print '__init__'
        if self.driver is None:
            # TODO: fix the phantomJS page rendering
            self.driver = webdriver.PhantomJS()
            #self.driver = webdriver.Chrome()
            self.driver.set_page_load_timeout(10)
            self.driver.set_window_size(1024, 768)

    def __enter__(self):
        print '__enter__'
        return self.driver

    def __exit__(self, type, value, traceback):
        print '__exit__'
        self.driver.service.process.send_signal(signal.SIGTERM)
        self.driver.quit()

    def get(self, url):
        print '__get__'
        self.driver.get(url)

def get(url):
    print 'Starting sp00ky'
    with Spooky() as s:
        s.get(url)

def xss_get(url):
    print 'starting xss payload'
    parsed = urlparse.urlparse(url)
    with Spooky() as s:
        # TODO: fix this cookie
        print url
        local_req = 'http://localhost:9091' + parsed.path
        print local_req
        s.get('http://localhost:9091/f4b79862d3dbfcc2c45ae07df16d0d6f')
        s.get(local_req)
