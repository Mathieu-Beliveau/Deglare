import os
import tensorflow as tf


class DatasetGenerator:
    def __init__(self, dataset_config):
        self.dc = dataset_config

    def get_dataset_from_generator(self):
        dir_list = os.listdir(self.dc.source_folder)
        return tf.data.Dataset.from_generator(self.image_tensor_generator, args=[len(dir_list)],
                                              output_signature=(tf.TensorSpec(shape=(self.dc.target_height,
                                                                                     self.dc.target_width, 3),
                                                                              dtype=tf.float32),
                                                                tf.TensorSpec(shape=(self.dc.target_height,
                                                                                     self.dc.target_width, 3),
                                                                              dtype=tf.float32)))

    def image_tensor_generator(self, stop):
        dir_list = os.listdir(self.dc.source_folder)
        i = 0
        while i < stop:
            file = dir_list[i]
            source_img = tf.io.read_file(self.dc.source_folder + file)
            target_img = tf.io.read_file(self.dc.target_folder + file)
            source_tensor = tf.cast(tf.image.decode_jpeg(source_img), tf.float32) / 255.0
            target_tensor = tf.cast(tf.image.decode_jpeg(target_img), tf.float32) / 255.0
            yield source_tensor, target_tensor
