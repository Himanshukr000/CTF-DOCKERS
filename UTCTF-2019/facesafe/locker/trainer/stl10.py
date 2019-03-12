import os
import urllib
import tarfile
import sys

from scipy.misc import imresize

import keras
import matplotlib.pyplot as plt
import numpy as np
from keras import backend as K, regularizers
from keras.callbacks import LearningRateScheduler
from keras.engine.training import Model
from keras.layers import Add, Conv2D, MaxPooling2D, Dropout, Flatten, Dense, BatchNormalization, Activation, Input
from keras.preprocessing.image import ImageDataGenerator

HEIGHT, WIDTH, DEPTH = 32, 32, 3

# number of classes in the STL-10 dataset.
N_CLASSES = 10

# size of a single image in bytes
SIZE = HEIGHT * WIDTH * DEPTH

# path to the directory with the data
DATA_DIR = './stl10_data'

# url of the binary data
DATA_URL = 'http://ai.stanford.edu/~acoates/stl10/stl10_binary.tar.gz'

# path to the binary train file with image data
TRAIN_DATA_PATH = DATA_DIR + '/stl10_binary/train_X.bin'

# path to the binary test file with image data
TEST_DATA_PATH = DATA_DIR + '/stl10_binary/test_X.bin'

DATA_BIN_PATH = DATA_DIR + '/stl10_binary.tar.gz'

# path to the binary train file with labels
TRAIN_LABELS_PATH = DATA_DIR + '/stl10_binary/train_y.bin'

# path to the binary test file with labels
TEST_LABELS_PATH = DATA_DIR + '/stl10_binary/test_y.bin'

# path to class names file
CLASS_NAMES_PATH = DATA_DIR + '/stl10_binary/class_names.txt'

def read_labels(path_to_labels):
    with open(path_to_labels, 'rb') as f:
        labels = np.fromfile(f, dtype=np.uint8)
        return labels

def resize(images, path):
    if images.shape[1] == 32 or images.shape[2] == 32:
        print("Not resizing images!")
        return images

    print("Resizing images")

    images_resized = np.zeros([0, 32, 32, 3], dtype=np.uint8)
    for image in range(images.shape[0]):
        temp = imresize(images[image], [32, 32, 3], 'bilinear') # TODO is this sizing right?
        images_resized = np.append(images_resized, np.expand_dims(temp, axis=0), axis=0)

    # Write out to path
    #with open(path, 'w') as f:
    #    images_resized.tofile(f)

    return images_resized

def read_all_images(path_to_data):
    with open(path_to_data, 'rb') as f:
        # read whole file in uint8 chunks
        everything = np.fromfile(f, dtype=np.uint8)

        # We force the data into 3x96x96 chunks, since the
        # images are stored in "column-major order", meaning
        # that "the first 96*96 values are the red channel,
        # the next 96*96 are green, and the last are blue."
        # The -1 is since the size of the pictures depends
        # on the input file, and this way numpy determines
        # the size on its own.

        needs_resize = True
        if needs_resize:
            images = np.reshape(everything, (-1, 3, 96, 96))
            images = np.transpose(images, (0, 3, 2, 1))
            images = resize(images, path_to_data)
            with open(path_to_data, 'w') as f:
                images.tofile(f)
        else:
            images = np.reshape(everything, (-1, 32, 32, 3))

        return images


def download():
    dest_directory = DATA_DIR
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
        
    filename = DATA_URL.split('/')[-1]
    filepath = os.path.join(dest_directory, filename)
    if not os.path.exists(filepath):
        def _progress(count, block_size, total_size):
            sys.stdout.write('\rDownloading %s %.2f%%' % (filename,
                                                          float(count * block_size) / float(total_size) * 100.0))
            sys.stdout.flush()

        filepath, _ = urllib.urlretrieve(DATA_URL, filepath, reporthook=_progress)
        print('Downloaded', filename)

def extract():
    dest_directory = DATA_DIR
    filename = DATA_URL.split('/')[-1]
    filepath = os.path.join(dest_directory, filename)
    tarfile.open(filepath, 'r:gz').extractall(dest_directory)


def load_dataset():
    # download the extract the dataset.
    if not os.path.exists(DATA_BIN_PATH):
        download()

    if not all((
        os.path.exists(TRAIN_DATA_PATH),
        os.path.exists(TRAIN_LABELS_PATH),
        os.path.exists(TEST_DATA_PATH),
        os.path.exists(TEST_LABELS_PATH),
    )):
        extract()

    # load the train and test data and labels.
    x_train = read_all_images(TRAIN_DATA_PATH)
    y_train = read_labels(TRAIN_LABELS_PATH)
    x_test = read_all_images(TEST_DATA_PATH)
    y_test = read_labels(TEST_LABELS_PATH)

    # convert all images to floats in the range [0, 1]
    #x_train = x_train.astype('float32')
    #x_train = (x_train - 127.5) / 127.5
    #x_test = x_test.astype('float32')
    #x_test = (x_test - 127.5) / 127.5

    # convert the labels to be zero based.
    y_train -= 1
    y_test -= 1

    print x_train.shape
    print y_train.shape

    print x_test.shape
    print y_test.shape

    return (x_train, y_train), (x_test, y_test)
