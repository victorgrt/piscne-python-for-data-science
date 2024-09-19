def slice_me(family: list, start: int, end: int) -> list:
    """
\033[1;33mslice_me\033[0m:
- \033[33mNAME: slice_me\033[0m
- \033[34mARG: list, int, int\033[0m
- \033[35mRETURN VALUE: list\033[0m
\033[1;37mTakes as parameters a 2D array, prints its shape, and returns a\
truncated version of the array based on the provided start and end \
arguments (slicing method).
- Checks arguments.
- Calculate the length of the 2d array and prints the shape.
- Trucante the list using the slicing method.
- Returns the new trucanted list.\033[0m
    """
    try:
        if not isinstance(family, list):
            raise AssertionError("\033[1;31mAssertionError: Bad Arguments !\
\nArguments needed are family: list, start: int, end: int\033[0m")

        if isinstance(start, int) is False or isinstance(end, int) is False:
            raise AssertionError("\033[1;31mAssertionError: Bad Arguments !\
\nArguments needed are family: list, start: int, end: int\033[0m")

        lenght = len(family[0])
        if not all(len(sublist) == lenght for sublist in family):
            raise AssertionError("\033[1;31mAssertionError: All sublist need\
 to be the same length !\033[0m")

        initial_shape = (len(family), lenght)
        print("My shape is :", initial_shape)

        trucanted_list = family[start:end]
        trucanted_shape = (len(trucanted_list), lenght)
        print("My new shape is :", trucanted_shape)

        return (trucanted_list)

    except AssertionError as error:
        print(error)


def main():
    pass


if __name__ == "__main__":
    main()
