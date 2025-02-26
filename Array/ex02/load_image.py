import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    ''' Load image from path and return it as numpy array '''
    img = Image.open(path)
    print(f"The shape of image is: {np.array(img).shape}\n {np.array(img)}")
    return np.array(img)
