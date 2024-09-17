from PIL import Image
import numpy


def ft_load(path: str) -> numpy.ndarray:
    """
\033[1;33mft_load\033[0m:
- \033[33mNAME: ft_load\033[0m
- \033[34mARG: str\033[0m
- \033[35mRETURN VALUE: array\033[0m
\033[1;37mLoads an image, prints its format, and its pixels\
content in RGB format.
- Loads an image using the ARG.
- Prints image's format.
- Prints a matrix of the image pixels in RGB.\033[0m
    """
    try:
        try:
            img = Image.open(path)
        except FileNotFoundError:
            raise AssertionError("FileNotFoundError")
        if path.endswith('.jpg') is False and path.endswith('.jpeg') is False:
            raise AssertionError("ExtensionError")
        print(f"The shape of the image is : ({img.size[1]},\
{img.size[0]}, {img.layers}) and is a .{img.format}")
        img_matrix = numpy.array(img)
        return (img_matrix)

    except AssertionError as error:
        if str(error) == "FileNotFoundError":
            return (print(f"\033[1;31mAssertionError: \
{path}: No such file or directory.\033[0m"))
        else:
            return (print(f"\033[1;31mAssertionError: \
{path}: Extension not supported.\033[0m"))


def main():
    print(ft_load("nordtest1.jpg"))


if __name__ == "__main__":
    main()
