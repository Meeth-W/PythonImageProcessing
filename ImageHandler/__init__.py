from PIL import Image
import numpy as np
from DataHandler import DataHandler

class ImageHandler:
    def __init__(self):
        """Initialize the ImageHandler with a DataHandler."""
        self.data_handler = DataHandler()

    def render_image_from_json(self, output_file='output_image.png'):
        """Renders an image from pixel data in JSON and saves it."""
        image_data = self.data_handler.load_pixel_data()

        width, height = image_data['width'], image_data['height']
        pixels = image_data['pixels']

        image_array = np.array(pixels, dtype=np.uint8)

        image = Image.fromarray(image_array)
        image.save(output_file)
        print(f"Image saved as {output_file}")

    def save_image_to_json(self, pixel_data, width, height):
        """Saves pixel data and dimensions to a JSON file."""
        image_data = {
            'width': width,
            'height': height,
            'pixels': pixel_data
        }
        self.data_handler.save_pixel_data(image_data)
