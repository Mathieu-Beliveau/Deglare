import os

import keras
import tensorflow as tf
from keras import layers


class Trainer:
    def __init__(self, dataset_config, dataset_generator):
        self.dc = dataset_config
        self.dataset_generator = dataset_generator

    def train(self):
        model = keras.models.Sequential([
            keras.layers.Conv2D(32, (3, 3), activation='relu',
                                input_shape=(self.dc.target_height, self.dc.target_width, 3)),
            keras.layers.MaxPool2D(2, 2),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.MaxPool2D(2, 2),
            keras.layers.Flatten(),
            keras.layers.Dropout(0.5),

            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(49152, activation='relu'),
            keras.layers.Reshape((self.dc.target_height, self.dc.target_width, 3))
        ])
        adam = tf.keras.optimizers.Adam()
        model.compile(loss='MeanSquaredError', optimizer=adam, metrics=['accuracy'])

        dir_list = os.listdir(self.dc.source_folder)
        items_count = len(dir_list)
        batch_size = 32
        num_batches = items_count / batch_size
        history = model.fit_generator(self.dataset_generator.get_dataset_from_generator(),
                                      epochs=10, steps_per_epoch=num_batches, verbose=1)
        x = 1
