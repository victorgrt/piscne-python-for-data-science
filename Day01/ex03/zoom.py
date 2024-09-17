from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_array = ft_load('animal.jpeg')
    if img_array is None:
        return

    zoomed_img_array = img_array[100:500, 500:800]
    print(f"New shape after slicing: {zoomed_img_array.shape}")
    print(zoomed_img_array[:5])

    plt.rcParams['toolbar'] = 'None' 
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('🦝 MR. RACOON 🦝')
    
    plt.rcParams['toolbar'] = 'None'
    ax.imshow(zoomed_img_array)
    plt.title('MR. RACOON')
    ax.set_aspect('auto')
    plt.show()


if __name__ == "__main__":
    main()