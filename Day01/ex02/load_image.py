from PIL import Image
import numpy


def ft_load(path: str) -> numpy.ndarray:
    """
\033[1;33mft_load\033[0m:
- \033[33mNAME: ft_load\033[0m
- \033[34mARG: str\033[0m
- \033[35mRETURN VALUE: array\033[0m
\033[1;37mloads an image, prints its format, and its pixels\
content in RGB format.
- .
- .
- .
- .\033[0m
    """
    try:
        try:
            img = Image.open(path)
        except FileNotFoundError:
            raise AssertionError("FileNotFoundError raised.")
        if path.endswith('.jpg') == False and path.endswith('.jpeg') == False:
            raise AssertionError("Wrong file extension")
        print(f"The shape of the image is : ({img.size[1]},\
{img.size[0]}, {img.layers}) and is a .{img.format}")
        img_matrix = numpy.array(img)
        return (img_matrix)

    except AssertionError as error:
        return (print(f"\033[1;31m{error}\nAssertionError:\
{path}: No such file or directory.\033[0m"))


def main():
    print(ft_load("nordtest1.jpg"))


if __name__ == "__main__":
    main()
