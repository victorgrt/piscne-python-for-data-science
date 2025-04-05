class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """static method to calculate dot product."""
        res = 0
        for x in range(0, len(V1)):
            res += float(V1[x] * V2[x])
        print("Dot Product is: ", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """static method to calculate addition."""
        vector = []
        for x in range(0, len(V1)):
            vector.append(float(V1[x] + V2[x]))
        print("Add Vector is: ", vector)


    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """static method to calculate soustraction."""
        vector = []
        for x in range(0, len(V1)):
            vector.append(float(V1[x] - V2[x]))
        print("Sous Vector is:", vector)
 

def main():
    pass


if __name__ == "__main__":
    main()
