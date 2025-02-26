import array
from PIL import Image
import numpy as np


def ft_invert(array) -> array:
    ''' Invert the colors of the image '''

    invert = array.copy()
    invert = 255 - invert

    image = Image.fromarray(invert)
    image.save("output_image_invert.jpg")
    return invert


def ft_red(array) -> array:
    ''' Keep only the red channel of the image '''

    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    red = red.astype(np.uint8)
    image = Image.fromarray(red)
    image.save("output_image_red.jpg")
    return red


def ft_green(array) -> array:
    ''' Keep only the green channel of the image '''

    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    green = green.astype(np.uint8)
    image = Image.fromarray(green)
    image.save("output_image_green.jpg")
    return green


def ft_blue(array) -> array:
    ''' Keep only the blue channel of the image '''

    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    image = Image.fromarray(blue)
    image.save("output_image_blue.jpg")
    return blue


def ft_grey(array: np.array) -> np.array:
    ''' Convert the image to greyscale '''

    gray = array.copy()
    gray_img = 0.2989 * gray[:, :, 0] + 0.5870 * gray[:, :, 1]\
        + 0.1140 * gray[:, :, 2]
    gray_img = gray_img.astype(np.uint8)
    image = Image.fromarray(gray_img)
    image.save("output_image_gray_numpy.jpg")
    return gray_img
