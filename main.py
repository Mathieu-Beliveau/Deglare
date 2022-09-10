import concurrent
import os
from random import random
import math
import tensorflow as tf

base_folder = '/home/strav/Dev/Data/Glare/'
target_folder = base_folder + 'target/'
source_folder = base_folder + 'source/'
raw_folder = base_folder + 'raw/'
target_width = 800
target_height = 600

def generate_dataset():
    dir_list = os.listdir(raw_folder)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(process_img, dir_list)


def process_img(raw_file):
    x1, y1, x2, y2 = generate_glare_coordinates()
    os.system("gimp -i -b '(resize \"{}\" \"{}\" {} {})' -b '(gimp-quit 0)'"
              .format(raw_folder + raw_file, target_folder + raw_file, target_width, target_height))
    os.system("gimp -i -b '(glare \"{}\" \"{}\" {} {} {} {})' -b '(gimp-quit 0)'"
              .format(target_folder + raw_file, source_folder + raw_file, x1, y1, x2, y2))


def generate_glare_coordinates():
    start_length = target_width + target_width * random()
    end_length = target_width * random()
    init_deg = random() * 2 * math.pi
    opposite_deg = init_deg + math.pi
    init_x = math.sin(init_deg) * start_length + (target_width / 2)
    init_y = math.cos(init_deg) * (target_width + target_width * 0.2) + (target_height / 2)
    opposite_x = math.sin(opposite_deg) * end_length + (target_width / 2)
    opposite_y = math.cos(opposite_deg) * end_length + (target_height / 2)
    return init_x, init_y, opposite_x, opposite_y


def get_dataset():
    source_img_tensors = []
    target_img_tensors = []
    dir_list = os.listdir(source_folder)
    for file in dir_list:
        source_img = tf.io.read_file(source_folder + file)
        target_img = tf.io.read_file(target_folder + file)
        source_img_tensors.append(tf.cast(tf.image.decode_jpeg(source_img), tf.float32) / 255.0)
        target_img_tensors.append(tf.cast(tf.image.decode_jpeg(target_img), tf.float32) / 255.0)
    return tf.data.Dataset.from_tensor_slices((source_img_tensors, target_img_tensors))


if __name__ == '__main__':
    generate_dataset()
    #dataset = get_dataset()