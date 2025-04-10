from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """La classe d'etre un Roi enfaite."""
    def __init__(self, first_name, is_alive=True):
        """Init using arguments. Super() is used \
        to get access to init from inherited class."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Setter for eyes attribute."""
        self.eyes = color

    def set_hairs(self, color: str):
        """Setter for hairs attribute."""
        self.hairs = color

    def get_eyes(self):
        """Getter for eyes attribute."""
        return self.eyes

    def get_hairs(self):
        """Getter for hairs attribute"""
        return self.hairs


def main():
    pass


if __name__ == "__main__":
    main()
