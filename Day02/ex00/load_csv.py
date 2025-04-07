import sys
import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
\033[1;33mload\033[0m:
- \033[33mNAME: load\033[0m
- \033[34mARG: str\033[0m
- \033[35mRETURN VALUE: pd.DataFrame\033[0m
\033[1;37mLoads a csv file and prints some infos.
- Loads the file from ARG.
- Prints infos.
- Returns the dataset.\033[0m
    """
    try:
        if os.path.isfile(path) is False:
            err = "\033[1;31mError raised : " + path + " not found\033[0m"
            raise AssertionError(err)
        if path.endswith('.csv') is False:
            err = "\033[1;31mError raised: Bad file extension\033[0m"
            raise AssertionError(err)
        if os.access(path, os.R_OK) is False:
            err = "\033[1;31mAssertionError: Bad permission.\033[0m"
            raise AssertionError(err)
        dataset = pd.read_csv(path)
        print("Loading dataset of dimensions ", dataset.shape, ".", sep="")

        return dataset
    except AssertionError as error:
        print(error)
        return
    return None


def main():
    try:
        if len(sys.argv) == 2:
            print(sys.argv)

            try:
                load(sys.argv[1])
            except AssertionError as error:
                print(error)
                return

        else:
            print("\033[1;31mAssertionError: Too many arguments\033[0m")
            raise AssertionError
    except AssertionError:
        return


if __name__ == "__main__":
    main()
