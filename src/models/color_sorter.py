
import os

from models import ImageFile

SRC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
STATIC_DIR = os.path.join(SRC_DIR, "src/static/wow_icons")
CSV_FILE = os.path.join(SRC_DIR, "data", "images.csv")


class ColorSorter:
    def __init__(self):
        self.image_files = self.read_csv_data()

    def rank_sort(self, color):
        """
        Takes the average color of an image (image.color) and sees how close it is to
        the color parameter.

        :param color: a HEX value color

        :return: sorted list of images
        """
        color = self.hex_to_rgb(color)
        c_r, c_g, c_b = color

        images = self.image_files

        for image in images:
            r, g, b = image.color
            image.rank = abs(r - c_r) + abs(g - c_g) + abs(b - c_b)

        images.sort(key=lambda i: i.rank)

        return images

    @staticmethod
    def hex_to_rgb(value):
        """
        Turns a HEX value into an RGB value
        :param value: hex string
        :return: RGB tuple (r, g, b)
        """
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def read_csv_data(self):
        """
        Read the csv file defined in `CSV_FILE` and create ImageFiles for each.

        Every CSV row is defined as such:
            ["filename of WoW icon", "red value", "green value", "blue value"]

        :return: a list of ImageFiles
        """
        with open(CSV_FILE, "r") as f:
            lines = f.readlines()

        images = []
        for line in lines:
            line = line.rstrip()
            data = line.split(",")

            filename = data[0]
            color = (int(data[1]), int(data[2]), int(data[3]))

            images.append(ImageFile(filename, color))

        return images
