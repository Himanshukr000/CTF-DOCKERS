'''
    Sanity check
'''

import locker.trainer.stl10 as stl10
import numpy as np
from scipy import misc
import keras

# Get data
(x_train, y_train), (x_test, y_test) = stl10.load_dataset()

# Load model
model = keras.models.load_model('locker/models/model.model')

# Measure accuracy
y_hat = model.predict_classes(x_test)

correct = 0
num_botched = 0

for prediction, actual in zip(y_hat, y_test):
    if prediction == actual:
        correct += 1

    if prediction == 1:
        num_botched += 1

print "\nAccuracy {}%".format(float(correct)/len(x_test)*100)
print "Number of Botched:", num_botched # Hopefully this is a very small number.

# Hopefully both of these are 1 as well.
botched_image = misc.imread('locker/models/random.png')
rand_prediction = model.predict_classes(np.array([botched_image]), verbose=0)

print "Sanity Prediction:", rand_prediction

solution = misc.imread('D:/Downloads/dog4.png')
# solution = misc.imread('../models/solution.png')
rand_prediction = model.predict_classes(np.array([solution]), verbose=0)
print "Solution Prediction:", rand_prediction