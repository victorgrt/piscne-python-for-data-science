def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
\033[1;33mgive_bmi\033[0m:
- \033[33mNAME: give_bmi\033[0m
- \033[34mARG: list[int|float], list[int|float]\033[0m
- \033[35mRETURN VALUE: list[int|float]\033[0m
\033[1;37m take 2 lists of integers or floats in input and returns a list\
of BMI values
- Checks arguments.
- Loops over all elements to calculate BMI.
- Returns list with results.\033[0m
    """
    try:
        for i in range(len(height)):
            if isinstance(height[i], list) is False:
                raise AssertionError(height[i])
            if isinstance(height[i], float) is False:
                raise AssertionError(height[i])
        for i in range(len(weight)):
            if isinstance(weight[i], int) is False:
                raise AssertionError(weight[i])
            if isinstance(weight[i], float) is False:
                raise AssertionError(weight[i])
        if len(height) != len(weight):
            raise AssertionError("\033[1;31mAssertionError: \
Both lists need to be the same size !\033[0m")

        new_list = [None] * len(weight)
        for j in range(len(height)):
            new_list[j] = height[j] * height[j]
            new_list[j] = weight[j] / new_list[j]

        return new_list

    except AssertionError as error:
        print("\033[1;31mAssertionError: '", error, "\
' is neither a int or a float !\033[0m", sep="")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
\033[1;33mapply_limit\033[0m:
- \033[33mNAME: apply_limit\033[0m
- \033[34mARG: list[int|float], limit\033[0m
- \033[35mRETURN VALUE: list[bool]\033[0m
\033[1;37m It returns a list of booleans (True if above the limit).
- Checks arguments.
- Loops over all elements to compare and fills a list with result.
- Returns bool list with results.\033[0m
    """
    try:
        if len(bmi) == 0 or bmi is None:
            raise AssertionError("\033[1;31mAssertionError: \
BMI list must not be empty!\033[0m")
        if not all(isinstance(x, (int, float)) for x in bmi):
            raise AssertionError("\033[1;31mAssertionError: \
BMI list must not be empty!\033[0m")
        if isinstance(limit, int) is False:
            raise AssertionError("\033[1;31mAssertionError: \
limit argument must be a positive int!\033[0m")
        if not all(x >= 0 for x in bmi) or limit < 0:
            raise AssertionError("\033[1;31mAssertionError: \
bmi and limit must be positive!\033[0m")

        bool_list = [None] * len(bmi)
        for i in range(len(bmi)):
            if bmi[i] > limit:
                bool_list[i] = True
            else:
                bool_list[i] = False
        return bool_list

    except AssertionError as error:
        print(error)


def main():
    height = [65]
    height.append(58)
    print("height:", height)

    weight = [180]
    weight.append(110)
    print("weight:", weight)

    give_bmi(height, weight)


if __name__ == "__main__":
    main()
