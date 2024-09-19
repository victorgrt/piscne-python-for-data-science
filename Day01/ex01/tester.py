from array2D import slice_me


def main():
    print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
    print(slice_me.__doc__)

    print("\033[1;32m# SUBJECT TESTER #\033[0m")
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("\033[1;31m# ERROR HANDLING #\033[0m")
    wrong_length = [[1.80, 78.4],
                    [2.15, 102.7, 100],
                    [2.10, 98.5],
                    [1.88, 75.2, 100]]
    print(slice_me(wrong_length, 0, 2))

    wrong_type = {"coucou": "les amis !"}
    print(slice_me(wrong_type, 0, 2))

    wrong_type2 = [[1.80, 78.4],
                   [2.15, 102.7],
                   [2.10, 98.5],
                   [1.88, 75.2]]
    print(slice_me(wrong_type2, "hey", "bien la mif?"))


if __name__ == "__main__":
    main()
