
import os


class ImageFile:
    def __init__(self, filename, color):
        """
        :param filename: string filename, must be PNG
        :param color: tuple of three colors in an RGB format
        """
        self.filename = os.path.basename(filename)
        self.color = color
        self.rank = 0

    @property
    def icon_name(self):
        return os.path.splitext(self.filename)[0]
