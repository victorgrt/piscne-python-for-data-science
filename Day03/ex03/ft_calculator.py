class calculator:
    
    def __init__(self, vector):
        """"""
        self.vector = vector
        
    
    def __add__(self, object) -> None:
        """"""
        self.vector = [number + object for number in self.vector]
        print(self.vector)
        return [number for number in self.vector]
            
    def __mul__(self, object) -> None:
        """"""
        self.vector = [number * object for number in self.vector]
        print(self.vector)
        return [number for number in self.vector]
    
    def __sub__(self, object) -> None:
        """"""
        self.vector = [number - object for number in self.vector]
        print(self.vector)
        return [number for number in self.vector]

    def __truediv__(self, object) -> None:
        """"""
        try:
            self.vector = [number / object for number in self.vector]
        except:
            return print("\033[31;1mZeroDivisionError: float division by zero\033[0m")        
        print(self.vector)    
        return [number for number in self.vector]
