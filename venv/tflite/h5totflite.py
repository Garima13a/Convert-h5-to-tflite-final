
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D,Conv2D
from keras import optimizers
import tensorflow as tf
from tensorflow.contrib import lite
import numpy as np
import keras
from keras.callbacks import ModelCheckpoint
from tensorflow.python.platform import gfile


# dimensions of our images.

img_width, img_height = 224, 224

train_data_dir = '/home/garima/Music/dogs-vs-cats/trainnew'
validation_data_dir = '/home/garima/Music/dogs-vs-cats/testnew'

# used to rescale the pixel values from [0, 255] to [0, 1] interval
datagen = ImageDataGenerator(rescale=1./255)

# automagically retrieve images and their classes for train and validation sets
train_generator = datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=16,
        class_mode='binary')

validation_generator = datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='binary')

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(img_width, img_height,3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1001, activation='softmax'))
#model.add(Activation('softmax'))

model.summary()
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
nb_epoch = 1
nb_train_samples = 63
nb_validation_samples = 55

model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples)
model.evaluate_generator(validation_generator, nb_validation_samples)




model.save('/home/garima/Music/dogs-vs-cats/models/fromsiraj.h5')
new_model = keras.models.load_model('/home/garima/Music/dogs-vs-cats/models/fromsiraj.h5')

converter = tf.lite.TocoConverter.from_keras_model_file('/home/garima/Music/dogs-vs-cats/models/fromsiraj.h5')
tflite_model = converter.convert()
open("/home/garima/Downloads/examples-master/lite/examples/image_classification/android/app/src/main/assets/from2.tflite", "wb").write(tflite_model)

