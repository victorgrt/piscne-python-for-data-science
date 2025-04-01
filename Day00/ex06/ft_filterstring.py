import sys
from ft_filter import ft_filter

def ft_filterstring():
    """
\033[1;33mft_filterstring\033[0m:
    - \033[33mNAME: ft_filterstring\033[0m
    - \033[34mARG: None\033[0m
    - \033[35mRETURN VALUE: None\033[0m
\033[1;37m- Parses arguments then calls ft_filter to filter and create new array according to lenght of words. Prints the new list.\033[0m
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Wrong number of arguments provided !\n\
    \033[3;32mUsage : python3 ft_filterstring.py <string> <int>\033[0m")

        string = sys.argv[1]
        try:
            _len = int(sys.argv[2])
        except ValueError:
            raise AssertionError("\033[31mPlease enter an int\033[3;32m\
            \nUsage : python3 ft_filterstring.py <string> <int> !\033[0m")
        if not isinstance(string, str) or not isinstance(_len, int):
            raise AssertionError()
        result = list(ft_filter(lambda string: len(string) > _len,
                      string.split()))
        print("filtered list:", result)

    except ValueError as error:
        print("\033[31mValueError:", error, "\n\033[3;32mUsage : python3 \
              ft_filterstring.py <string> <int> !\033[0m")
    except AssertionError as error:
        print("\033[31mAssertionError:", error)

def main():
    ft_filterstring()


if __name__ == "__main__":
    main()
