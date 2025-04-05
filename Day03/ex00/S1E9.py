from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Init attributes using arguments."""
        self.name = first_name
        self.is_alive = is_alive

    def die(self):
        """No need to do it here right?"""
        pass
    
class Stark(Character):


    def __init__(self, first_name: str, is_alive=True):
        """Init attributes using arguments."""
        self.name = first_name
        self.is_alive = is_alive
        
        
    def die(self):
        """Changes is_alive attribute to False."""
        self.is_alive = False


def main():
    Perso = Stark("Kirikou", True)
    print(Perso)
    print(Perso._name)
    print(Perso._is_alive)
    Perso.die()
    print(Perso._is_alive)
    

if __name__ == "__main__":
    main()
