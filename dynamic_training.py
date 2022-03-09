import config
import os
from django import conf
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D, Dropout
#from keras.optimizers import Adam, SGD
from tensorflow.keras.optimizers import Adam, SGD
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
import itertools
import random
import warnings
import numpy as np
import cv2
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import ModelCheckpoint, EarlyStopping
warnings.simplefilter(action='ignore', category=FutureWarning)


MODEL = "CUSTOM_DATA"
train_path = config.MODEL_CONFIGS[MODEL][1]
test_path = config.MODEL_CONFIGS[MODEL][2]

classes = len(next(os.walk(train_path))[1])

train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(
    directory=train_path, target_size=(64, 64), class_mode='categorical', batch_size=10, shuffle=True)
test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(
    directory=test_path, target_size=(64, 64), class_mode='categorical', batch_size=10, shuffle=True)

imgs, labels = next(train_batches)

model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(3, 3),
          activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))

model.add(Conv2D(filters=64, kernel_size=(3, 3),
          activation='relu', padding='same'))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))

model.add(Conv2D(filters=128, kernel_size=(3, 3),
          activation='relu', padding='valid'))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))

model.add(Flatten())

model.add(Dense(64, activation="relu"))
model.add(Dense(128, activation="relu"))
# model.add(Dropout(0.2))
model.add(Dense(128, activation="relu"))
# model.add(Dropout(0.3))

# Put Value here if added a new image
model.add(Dense(classes, activation="softmax"))


model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy', metrics=['accuracy'])
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss', factor=0.2, patience=1, min_lr=0.0001)
early_stop = EarlyStopping(
    monitor='val_loss', min_delta=0, patience=2, verbose=0, mode='auto')


model.compile(optimizer=SGD(learning_rate=0.001),
              loss='categorical_crossentropy', metrics=['accuracy'])
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss', factor=0.2, patience=1, min_lr=0.0005)
early_stop = EarlyStopping(
    monitor='val_loss', min_delta=0, patience=2, verbose=0, mode='auto')


history2 = model.fit(train_batches, epochs=10, callbacks=[
                     reduce_lr, early_stop],  validation_data=test_batches)  # , checkpoint])
imgs, labels = next(train_batches)  # For getting next batch of imgs...

imgs, labels = next(test_batches)  # For getting next batch of imgs...
scores = model.evaluate(imgs, labels, verbose=0)

model.save(config.MODEL_CONFIGS[MODEL][0])
