from __future__ import print_function

from locker.constants import BOTCHED_INDEX

'''
    This solves the puzzle using gradient ascent.
    Essentially tries to find an image that maximize the activation to the given class.
    Based on https://blog.keras.io/how-convolutional-neural-networks-see-the-world.html
'''

import keras
from keras import backend as K
K.set_learning_phase(0) # Known issue https://github.com/fchollet/keras/issues/2310

from scipy.misc import imsave
import numpy as np

img_width = 32
img_height = 32

layer_name = 'predictions'
filter_index = BOTCHED_INDEX # The class we want to maximize.
iterations = 50000

def deprocess_image(x):
    # normalize tensor: center on 0., ensure std is 0.1
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1

    # clip to [0, 1]
    x += 0.5
    x = np.clip(x, 0, 1)

    # convert to RGB array
    x *= 255
    if K.image_data_format() == 'channels_first':
        x = x.transpose((1, 2, 0))
    x = np.clip(x, 0, 255).astype('uint8')
    return x

model = keras.models.load_model('locker/models/model.model')
print('Model loaded.')

model.summary()

# this is the placeholder for the input images
input_img = model.input

# get the symbolic outputs of each "key" layer (we gave them unique names).
layer_dict = dict([(layer.name, layer) for layer in model.layers[1:]])

def normalize(x):
    # utility function to normalize a tensor by its L2 norm
    return x / (K.sqrt(K.mean(K.square(x))) + 1e-5)

# we build a loss function that maximizes the activation
# of the nth filter of the layer considered
layer_output = layer_dict[layer_name].output
loss = K.mean(model.output[:, filter_index])

# we compute the gradient of the input picture wrt this loss
grads = K.gradients(loss, input_img)[0]

# normalization trick: we normalize the gradient
grads = normalize(grads)

# this function returns the loss and grads given the input picture
iterate = K.function([input_img], [loss, grads])

# step size for gradient ascent
step = 1.

# we start from a gray image with some random noise
if K.image_data_format() == 'channels_first':
    input_img_data = np.random.random((1, 3, img_width, img_height))
else:
    input_img_data = np.random.random((1, img_width, img_height, 3))
input_img_data = (input_img_data - 0.5) * 20 + 128

# we run gradient ascent for 20 steps
for i in range(iterations):
    loss_value, grads_value = iterate([input_img_data])
    input_img_data += grads_value * step

    print('Current loss value:', loss_value)
    if loss_value <= 0.:
        # some filters get stuck to 0, we can skip them
        break
    if loss_value > 0.999:
        break

# decode the resulting input image
img = deprocess_image(input_img_data[0])
imsave('solution.png', img)

print("Solved image prediction:", np.argmax(model.predict(np.array([img]))))