from flask import Flask
app = Flask(__name__)

app.config['APP_NAME'] = 'FaceSafe'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 #2MB max

# Debug
#app.config['TEMPLATES_AUTO_RELOAD'] = True
#app.config['DEBUG'] = True

import locker.controllers # registers controllers