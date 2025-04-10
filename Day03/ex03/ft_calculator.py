class calculator:
    """Calculator class with methods to calculate"""
    def __init__(self, vector):
        """Inits the class with content inside a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds vector content."""
        self.vector = [number + object for number in self.vector]
        print(self.vector)
        return [number for number in self.vector]

    def __mul__(self, object) -> None:
        """Multiplies vector content."""
        self.vector = [number * object for number in self.vector]
        print(self.vector)
        return [number for number in self.vector]

    def __sub__(self, object) -> None:
        """Substract vector content."""
        self.vector = [number - object for number in self.vector]
        print(self.vector)
        return [number for number in self.vector]

    def __truediv__(self, object) -> None:
        """Divids vector content."""
        try:
            self.vector = [number / object for number in self.vector]
        except ZeroDivisionError:
            return print("\033[31;1mZeroDivisionError: \
float division by zero\033[0m")
        print(self.vector)
        return [number for number in self.vector]


def main():
    pass


if __name__ == "__main__":
    main()
