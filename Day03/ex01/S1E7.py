from S1E9 import Character


class Baratheon(Character):
    """Representating the Baratheon family."""
    
    def __init__(self, first_name: str, is_alive=True):
        """Init attributes using arguments. Super is used to get access to init."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


    def die(self):
        """Sets is_alive to False."""
        self.is_alive = False


class Lannister(Character):
    """Representating the Lanister family."""
    def __init__(self, first_name: str, is_alive=True):
        """Init attributes using arguments. Super is used to get access to init."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    def die(self):
        """Sets is_alive to False."""
        self.is_alive = False
    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Create an instance. cls to call a class i think?"""
        instance = cls(first_name)
        instance.is_alive = is_alive        
        return instance
    
    
def main():
    pass


if __name__ == "__main__":
    main()