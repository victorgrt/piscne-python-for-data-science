import time
import shutil
from random import randrange


def ft_tqdm(lst: range) -> None:
    """
\033[1;32mFT_TQDM\033[0m:
    - \033[33mNAME: ft_tqdm\033[0m
    - \033[34mARG: range\033[0m
    - \033[35mRETURN VALUE: None\033[0m
\033[1;37mThis function is a copy of tqdm :
    - Prints the % that's done compared with ARG.
    - Dinamically prints a loading bar using ARG as a max value to go to.
    - Prints number of iterations that was done.
    - Prints the time current time of execution then the time it took.
    - Changes the color every iteration.\033[0m
    """

    try:
        if type(lst) is not range:
            raise AssertionError("\033[1;31mAssertionError:\
Argument has to be a range() !\033[0m")
        if lst == range(0, 0):
            raise ValueError("\033[1;31mValueError: Invalid Range !\033[0m")
        if max(lst) > 1000000:
            raise ValueError("\033[1;31mValueError: Invalid Range !\033[0m")

        max_range = max(lst) + 1
        max_width = shutil.get_terminal_size().columns - 30
        start_time = time.time()

        for i, res in enumerate(lst, start=1):
            pourcentage = int((i + 1) / max_range * 100)
            filled = int(max_width * (i + 1) // max_range)
            bar = '█' * filled + ' ' * (max_width - filled)
            passed_time = float(time.time() - start_time)
            random_color = "\033[1;" + str(randrange(30, 36)) + 'm'

            print(f"\r{random_color}{pourcentage}%|{bar}\
| {i}/{max_range} [{passed_time:.2f}s]\033[0m", end="", flush=True)
            yield res

    except AssertionError as error:
        print(error)
    except ValueError as error:
        print(error)
        print("\033[1;31mARG : (1 > range < 1000000)\033[0m")


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()
