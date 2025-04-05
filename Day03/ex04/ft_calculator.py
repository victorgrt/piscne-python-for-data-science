class calculator:
    
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """"""
        vector = []
        for x in range(0, len(V1)):
            vector.append(float(V1[x] * V2[x]))
        res = 0
        for num in vector:
            res += num 
        
        print("Dot Product is: ", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """"""
        vector = []
        for x in range(0, len(V1)):
            vector.append(float(V1[x] + V2[x]))
        print("Add Vector is: ", vector)


    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """"""
        vector = []
        for x in range(0, len(V1)):
            vector.append(float(V1[x] - V2[x]))
        print("Sous Vector is:", vector)
    