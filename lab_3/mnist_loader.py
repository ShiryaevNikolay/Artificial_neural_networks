import itertools
import zipfile
from PIL import Image


def load_data():
    with zipfile.ZipFile("../mnist_train.zip", "r") as archive:
        for filename in archive.namelist():
            training_data = []
            with archive.open(filename) as file:
                img = Image.open(file)
                pixels = img.load()
                for x, y in itertools.product(range(img.size[0]), range(img.size[1])):
                    training_data.append(pixels[x, y])
