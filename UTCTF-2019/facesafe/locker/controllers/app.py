from locker import app

import os

from flask import (
    send_from_directory,
    request,
    render_template,
    jsonify
)

from locker import app

import keras
import numpy as np
from scipy.misc import imread, imresize
import json

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory("static", "robots.txt")

print("Initializing model")
current_file = os.path.join('locker/models', 'model.model')
model = keras.models.load_model(current_file)

@app.route('/api/check', methods = ['POST'])
def check():        
    if 'image' not in request.files:
        return json.dumps({"error": "No image provided"}), 200
    image = imread(request.files['image'], mode='RGB')
    width, height, channels = image.shape
    if not channels == 3:
        return json.dumps({"error": "Image is invalid."}), 200
    if width > 1024 or height > 1024:
        return json.dumps({"error": "Image is too large!"}), 200
    if not (width == 32 and height == 32):
        image = imresize(image, (32, 32))

    CLASSES = ['Mr. Airplane', 'Ms. Automobile', 'Ms. Bird', 'Mr. Cat', 
    'Mr. Deer [VIP]', 'Mr. Dog', 'Mr. Frog', 'Mrs. Horse', 'Mrs. Ship', 'Ms. Truck']
    SECRETS = ['VROOM VROOM AIRPLANE SECRET', 'SKRRT SKRRT I AM A CAR', 'TWEET TWEET TWEET', 'MEOWWWW',
    'Why are all these users so degenerate? I actually have something intelligent to store: utflag{n3ur4l_n3t_s3cur1ty_b4d_p4d1ct4b1l1ty}',
    "WOOF WOOF ARF ARF ARF", "RIBBBBBBITTTT", "NEIGGGHHHH", "HONK HONK", "VROOM VROOM"]
    index = int(model.predict_classes(np.array([image]), verbose=0)[0])
    prediction = CLASSES[index]

    return jsonify(json.dumps({"user": CLASSES[index], "secret": SECRETS[index]})), 200

@app.route('/api/model/model_metadata.json')
def model_json():
    return send_from_directory("models", "model_metadata.json")

@app.route('/api/model/model.model')
def model_weights():
    return send_from_directory("models", "model.model")