from load_image import ft_load


def main():
    print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
    print(ft_load.__doc__)

    print("\033[1;32m# BASIC TEST #\033[0m")
    print(ft_load("landscape.jpg"))

    print(ft_load("animal.jpeg"))

    print(ft_load("vgoret.jpg"))

    print("\n\033[1;31m# ERROR HANDLING #\033[0m", end="\n")
    print(ft_load("coucou.jpg"))
    print(ft_load("animal.jpg"))
    print(ft_load("nordtest1.png"))


if __name__ == "__main__":
    main()
