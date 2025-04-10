import sys

def ft_statistics(*args: any, **kwargs: any) -> None:
    num_len = len(args)
    key_words = ["median", "std", "var", "mean", "quartile"]
   
    def ft_median(nums) -> int:
        size = len(nums)
        if size % 2 == 0:
            median = size / 2
            return new_list[int(median - 1)]
        else:
            median = (size + 1) / 2
            return new_list[int(median - 1)]
    
    def ft_std():
        pass

    def ft_var(nums):
        mean = ft_mean(nums)
        toto = 0
        for num in nums:
            toto += (num - mean) ** 2
        size = len(nums)
        res = toto / (size)
        return res


    def ft_mean(nums):
        size = len(nums)
        res = 0
        for num in nums:
            res += num
        return res / size


    def ft_quartile():
        pass
    
    

    new_list = list(args)
    print("New list:", new_list, type(new_list))
    for word in kwargs.values():
        match word:
            case "median":
                result = ft_median(new_list)
                print(result)
            case "std":
                ft_std()
            case "var":
                result = ft_var(new_list)
                print(result)    
            case "mean":
                result = ft_mean(new_list)
                print(result)
            case "quartile":
                ft_quartile()
            case _:
                print("!!key word not found!!")


    

def main():
    #check args
    # ft_statistics(2, 1, 52, 4, 5, toto="median", maybe="quartile", var="var", std="std", mean="mean", _not="blabla")
    # ft_statistics(10, 2, 38, 23, 38, 21, 25, 26, 244, toto="mean")
    # ft_statistics(10, 2, 38, 23, 38, 21, 25, 26, 244, toto="median")
    # ft_statistics(555, 2, 10, 21, 23, 25, 26, 38, 38, 244, toto="var")
    # ft_statistics(2, 1, 52, 4, 5, var="var")
    
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, world="var")

    
    
if __name__ == "__main__":
    main()