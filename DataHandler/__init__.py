import json
import os

class DataHandler:
    def __init__(self, data_file='data.json'):
        """Initialize with the path to the JSON file."""
        self.data_file = os.path.join(os.path.dirname(__file__), data_file)

    def load_pixel_data(self):
        """Loads pixel data from the JSON file."""
        with open(self.data_file, 'r') as json_file:
            return json.load(json_file)

    def save_pixel_data(self, image_data):
        """Saves pixel data to the JSON file."""
        with open(self.data_file, 'w') as json_file:
            json.dump(image_data, json_file, indent=4)
