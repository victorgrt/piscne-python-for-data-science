from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
\033[1mInverts the color of the image received\033[0m.
    """
    inverted = 255 - array
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array) -> np.ndarray:
    """
\033[1;31mChanges pixels color to RED.\033[0m
    """
    clear_red_channel = array[:, :, 0]
    red_array = np.zeros_like(array)
    red_array[:, :, 0] = clear_red_channel
    Image.fromarray(red_array).show()

    return (red_array)


def ft_blue(array) -> np.ndarray:
    """
\033[1;34mChanges pixels color to BLUE.\033[0m
    """
    clear_blue_channel = array[:, :, 2]
    blue_channel = np.zeros_like(array)
    blue_channel[:, :, 2] = clear_blue_channel
    Image.fromarray(blue_channel).show()

    return (blue_channel)


def ft_green(array) -> np.ndarray:
    """
\033[1;32mChanges pixels color to GREEN.\033[0m
    """
    clear_green_channel = array[:, :, 1]
    green_channel  = np.zeros_like(array)
    green_channel[:, :, 1] = clear_green_channel
    Image.fromarray(green_channel).show()
    return (green_channel)


# def ft_gray(array) -> np.ndarray:
#     """
# \033[1;31mChanges pixels color to GRAY.\033[0m
#     """