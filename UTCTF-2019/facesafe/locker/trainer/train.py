'''
    Trains our model.
'''
import keras
import data
import model as mo

def train_model(save_file, random_file='random.png', epochs=5):
    batch_size = 32

    x_train, y_train, x_test, y_test = data.prepare_data(random_file)

    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    model = mo.build_model(x_train.shape[1:])

    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['categorical_accuracy'])


    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_data=(x_test, y_test))

    s, accuracy = model.evaluate(x_test, y_test)

    if accuracy < 0.5:
      print("Model is not accurate! Will retry")
      return False

    model.save(save_file)
    print("Model has been saved to {}".format(save_file))
    return True

if __name__ == "__main__":
    train_model('model')