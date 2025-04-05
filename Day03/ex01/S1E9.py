from abc import ABC, abstractmethod


class Character(ABC):
    """
    """
    @abstractmethod
    def __init__(self, first_name: str, family_name:str , is_alive=True):
        """
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name

    def die(self):
        """
        """
        pass
    
    def __str__(self):
        """"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __repr__(self):
        """"""
        return self.__str__()

    

class Stark(Character):
    """
    """
    def __init__(self, first_name: str, is_alive=True):
        """
        """
        self.first_name = first_name
        self.is_alive = is_alive
        
        
    def die(self):
        """
        """
        self.is_alive = False
        

def main():
    Perso = Stark("Kirikou", True)
    print(Perso)
    print(Perso.first_name)
    print(Perso.is_alive)
    Perso.die()
    print(Perso.is_alive)
    

if __name__ == "__main__":
    main()