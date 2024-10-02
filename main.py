import random
from ImageHandler import ImageHandler

def generate_random_pixel_data(width, height):
    """Generate random RGB pixel data for an image."""
    return [[[random.randint(0, 255) for _ in range(3)] for _ in range(width)] for _ in range(height)]

def main():
    image_handler = ImageHandler()

    width, height = 128, 128
    random_pixel_data = generate_random_pixel_data(width, height)

    image_handler.save_image_to_json(random_pixel_data, width, height)
    image_handler.render_image_from_json()

if __name__ == '__main__':
    main()