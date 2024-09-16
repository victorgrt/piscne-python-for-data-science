import sys


def printResult(object: list) -> None:
    """
\033[1;33mprintResult\033[0m:
    - \033[33mNAME: printResult\033[0m
    - \033[34mARG: list\033[0m
    - \033[35mRETURN VALUE: None\033[0m
\033[1;37mDisplays the sums of its upper-case characters, lower-case characters\
, punctuation characters, digits and spaces.
    - Displays the sums of all characters contained in ARG.\033[0m
    """
    print("\033[1mThe text contains\033[32m", object[0],
          '\033[0m\033[1mcharacters:\033[0m')
    print("\033[3m\033[33m  -", object[2], "upper letters.")
    print("\033[3m\033[36m  -", object[1], "lower letters.")
    print("\033[3m\033[31m  -", object[4], "punctuation marks.")
    print("\033[3m\033[32m  -", object[3], "spaces.")
    print("\033[3m\033[35m  -", object[5], "digits.")


def examinateString() -> None:
    try:
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: Wrong number of arguments provided !")

        if (len(sys.argv) == 1):
            string = input('\033[1;34mPlease enter the string you wanna examine!\033[0m\
\n😎👉:')
        else:
            string = sys.argv[1]
        ponctuation = [',', '.', '!', '?', ';', ':']
        total = 0
        upper = 0
        lower = 0
        space = 0
        ponct = 0
        digit = 0
        for a in string:
            if (a.isupper() is True):
                upper += 1
            elif (a.islower() is True):
                lower += 1
            elif (a.isspace() is True):
                space += 1
            elif (a in ponctuation):
                ponct += 1
            elif (a.isdigit() is True):
                digit += 1
            total += 1
        toPrint = [total, lower, upper, space, ponct, digit]
        printResult(toPrint)
    
    except AssertionError as error:
        print("\033[1;31m", error, "\033[0m", sep="")
        print("\033[1;31mUsage: python3 building.py or python3 building.py <string>\033[0m", sep="")


def main():
    examinateString()

if __name__ == "__main__":
    main()
