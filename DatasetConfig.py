class DatasetConfig:
    def __init__(self, base_folder, target_width, target_height):
        self.target_width = target_width
        self.target_height = target_height
        self.base_folder = base_folder
        self.raw_files_folder = self.base_folder + 'raw/'
        self.target_folder = self.base_folder + 'target/'
        self.source_folder = self.base_folder + 'source/'