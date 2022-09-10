import concurrent
import math
import os
from random import random


class GlareGenerator:
    def __init__(self, dataset_config):
        self.dc = dataset_config

    def generate_dataset(self):
        dir_list = os.listdir(self.dc.raw_files_folder)
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.process_img, dir_list)

    def process_img(self, raw_file):
        x1, y1, x2, y2 = self.generate_glare_coordinates()
        os.system("gimp -i -b '(resize \"{}\" \"{}\" {} {})' -b '(gimp-quit 0)'"
                  .format(self.dc.raw_files_folder + raw_file,
                          self.dc.target_folder + raw_file,
                          self.dc.target_width,
                          self.dc.target_height))
        os.system("gimp -i -b '(glare \"{}\" \"{}\" {} {} {} {})' -b '(gimp-quit 0)'"
                  .format(self.dc.target_folder + raw_file,
                          self.dc.source_folder + raw_file, x1, y1, x2, y2))

    def generate_glare_coordinates(self):
        start_length = self.dc.target_width + self.dc.target_width * random()
        end_length = self.dc.target_width * random()
        init_deg = random() * 2 * math.pi
        opposite_deg = init_deg + math.pi
        init_x = math.sin(init_deg) * start_length + (self.dc.target_width / 2)
        init_y = math.cos(init_deg) * (self.dc.target_width + self.dc.target_width * 0.2) + (self.dc.target_height / 2)
        opposite_x = math.sin(opposite_deg) * end_length + (self.dc.target_width / 2)
        opposite_y = math.cos(opposite_deg) * end_length + (self.dc.target_height / 2)
        return init_x, init_y, opposite_x, opposite_y
