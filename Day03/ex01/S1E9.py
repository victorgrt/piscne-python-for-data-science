from abc import ABC, abstractmethod


class Character(ABC):


    @abstractmethod
    def __init__(self, first_name: str, family_name:str , is_alive=True):
        """Init attributes using arguments."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name


    def die(self):
        """No need here"""
        pass

    
    def __str__(self):
        """Overwrite __str__ method to custom value."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    
    def __repr__(self):
        """Replace default __str__ with overwritten one."""
        return self.__str__()


class Stark(Character):


    def __init__(self, first_name: str, is_alive=True):
        """Init attributes using arguments"""
        self.first_name = first_name
        self.is_alive = is_alive
        
        
    def die(self):
        """Changes is_alive attribute to False"""
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