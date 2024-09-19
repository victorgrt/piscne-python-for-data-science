from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


array = ft_load("landscape.jpg")
# Image.fromarray(array).show()


def ft_invert(array) -> array:
    inverted = 255 - array
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array) -> array:
    clear_red_channel = array[:, :, 0]
    red_array = np.zeros_like(array)
    red_array[:, :, 0] = clear_red_channel
    Image.fromarray(red_array).show()

    return (red_array)

# ft_red(array)

def ft_blue(array) -> array:
    clear_blue_channel = array[:, :, 2]
    blue_channel = np.zeros_like(array)
    blue_channel[:, :, 2] = clear_blue_channel
    Image.fromarray(blue_channel).show()

    return (blue_channel)

# ft_blue(array)


def ft_green(array) -> array:
    clear_green_channel = array[:, :, 1]
    green_channel  = np.zeros_like(array)
    green_channel[:, :, 1] = clear_green_channel
    Image.fromarray(green_channel).show()

    return (green_channel)

ft_green(array)
# def ft_blue(array) -> array:
#     pass


# def ft_grey(array) -> array:
#     pass

# ft_invert(array)