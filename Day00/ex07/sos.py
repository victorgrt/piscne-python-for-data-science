import sys


def string_to_morse(string: str) -> None:
    """
\033[1;33mstring_to_morse\033[0m:
    - \033[33mNAME: MAIN\033[0m
    - \033[34mARG: None\033[0m
    - \033[35mRETURN VALUE: None\033[0m
\033[1;37mThis program takes a string as an argument and encodes\
it into Morse Code:
    - Check the argument.
    - Creates a dictionnary containing all accepted characters.
    - Loops over all characters in the string and encodes them\
using the dictionnary.\033[0m
    """

    morse_code = {" ": "/", "A": ".-", "B": "-...",
                  "C": "-.-.", "D": "-..", "E": ".",
                  "F": "..-.",  "G": "--.",  "H": "....",
                  "I": "..", "J": ".---", "K": "-.-",
                  "L": ".-..", "M": "--", "N": "-.",
                  "O": "---", "P": ".--.", "Q": "--.-",
                  "R": ".-.", "S": "...", "T": "-",
                  "U": "..-", "V": "...-", "W": ".--",
                  "X": "-..-", "Y": "-.--", "Z": "--..",
                  "0": "-----", "1": ".----", "2": "..---",
                  "3": "...--", "4": "....-", "5": ".....",
                  "6": "-....", "7": "--...", "8": "---..",
                  "9": "----."}

    for c in string:
        if c not in morse_code and c.upper() not in morse_code:
            error_string = c + " is not a valid character.\
                \nAccepted Values : A-Z, a-z and 0-9"
            raise AssertionError(error_string)

    i = 0
    for c in string:
        if c not in morse_code:
            print(morse_code[c.upper()], end='')
        else:
            print(morse_code[c], end='')
        if i != len(string) - 1:
            print(" ", end='')
        i += 1


def main():
    try:
        if len(sys.argv) != 2:
            if len(sys.argv) < 2:
                raise AssertionError("Wrong number of arguments :\
at least one (1) argument is needed !")
            else:
                raise AssertionError("Wrong number of arguments :\
only one (1) argument is needed !")

        string = sys.argv[1]

        if not isinstance(sys.argv[1], str):
            raise ValueError("Wrong type of argument : string is required !")

        string_to_morse(string)

    except AssertionError as error:
        print("\033[1;31mAssertionError:", error)


if __name__ == "__main__":
    main()
