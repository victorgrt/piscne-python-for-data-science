from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def __init__(self, first_name: str, family_name: str, is_alive=True):
        """Init values of atributes of class."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name

    def die(self):
        """No need to change it here as it will be changed in subclasses."""
        pass

    def __str__(self):
        """Change __str__ return value of class."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Change __str__ of class."""
        return self.__str__()


class Stark(Character):
    def __init__(self, first_name: str, is_alive=True):
        """Init first name and is_alive according to args."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Changes is_alive to False."""
        self.is_alive = False


def main():
    pass


if __name__ == "__main__":
    main()
