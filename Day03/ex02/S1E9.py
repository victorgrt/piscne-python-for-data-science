
from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character with name and isalive attributes."""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Character Class"""
        self.name = first_name
        self.is_alive = is_alive

    def die(self):
        """Will be implemented in subclasses."""
        pass

    def __str__(self):
        """Overwrite __str__ method to custom value."""
        return f"Vector: \
    ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Replace default __str__ with overwritten one."""
        return self.__str__()


class Stark(Character):
    """Stark Class, subclass from Character"""
    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Stark Class"""
        self.name = first_name
        self.is_alive = is_alive

    def die(self):
        """Changes is_alive attribute to False."""
        self.is_alive = False


def main():
    pass


if __name__ == "__main__":
    main()
