import binascii
import hashlib
import datetime
import base64
import random
import os
import pickle

from flask import Flask, request, make_response, render_template
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS

from database import init_db, db_session
from models import Device

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

FLAG = os.getenv('FLAG') or 'SEA{intriguing_idawwr}SIDES'

ADMIN_INDEX = 45

def id_transform(index):
    md5 = hashlib.md5()
    md5.update(str(index).encode())
    return binascii.hexlify(md5.digest()).decode()

def initialize_db():
    init_db()
    Device.query.delete()

    statuses = [
        'UPDATING',
        'CONNECTING',
        'CONNECTED',
    ]

    for index in range(0, 100):
        status = random.sample(statuses, 1)[0]
        device = Device(uuid=id_transform(index), status=status, last_tick=datetime.datetime.utcnow())
        db_session.add(device)
    
    db_session.commit()
    device = Device.query.all()
    admin_device = device[ADMIN_INDEX]
    admin_device.admin = True
    admin_device.status = FLAG

    db_session.commit()

# init_db()
initialize_db()

class DeviceReader(Resource):
    """
        read device data
    """

    def get(self, device_id):
        try:
            device = Device.query.filter_by(uuid=device_id)[0]
            return {
                'status': device.status,
                'last_tick': str(device.last_tick),
                'admin': device.admin,
                'uuid': device.uuid
            }
        except:
            return abort(400, message="Couldn't Find ID")

        return response

api.add_resource(DeviceReader, '/device/<string:device_id>')

if __name__ == '__main__':
    app.run(debug=True)