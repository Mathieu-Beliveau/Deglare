from DatasetConfig import DatasetConfig
from DatasetGenerator import DatasetGenerator
from GlareGenerator import GlareGenerator
from Trainer import Trainer

if __name__ == '__main__':
    target_width = 128
    target_height = 128
    dc = DatasetConfig('/home/strav/Dev/Data/Glare/', target_width=target_width, target_height=target_height)
    glare_generator = GlareGenerator(dc)
    glare_generator.generate_dataset()
    # dataset_generator = DatasetGenerator(dc)
    # trainer = Trainer(dc, dataset_generator)
    # trainer.train()
