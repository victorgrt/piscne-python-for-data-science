import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Wrong number of arguments provided !\\n\
            \033[3;32mUsage : python3 ft_filterstring.py <string> <int>\
            \033[0m")

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


if __name__ == "__main__":
    main()
