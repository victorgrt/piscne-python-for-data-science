from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_grey
import sys


array = ft_load("landscape.jpg")


def main():
    if len(sys.argv) == 1:
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
        print(ft_green.__doc__)
        print(ft_blue.__doc__)
        print(ft_red.__doc__)
        print(ft_grey.__doc__)
    elif len(sys.argv) == 2:
        if (str(sys.argv[1]) == "grey"):
            ft_grey(array)
            print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
            print(ft_grey.__doc__)
        elif (str(sys.argv[1]) == "green"):
            ft_green(array)
            print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
            print(ft_green.__doc__)
        elif (str(sys.argv[1]) == "red"):
            ft_red(array)
            print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
            print(ft_red.__doc__)
        elif (str(sys.argv[1]) == "blue"):
            ft_blue(array)
            print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
            print(ft_blue.__doc__)
        elif (str(sys.argv[1]) == "inverted"):
            ft_invert(array)
            print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
            print(ft_invert.__doc__)
        else:
            print("\033[1;31mBad argument : only inverted, green, red, blue and grey are accepted !\033[0m")
        return
    else:
        print("\033[1;31mWrong number of arguments.\033[0m")
        return
    


if __name__ == "__main__":
	main()
