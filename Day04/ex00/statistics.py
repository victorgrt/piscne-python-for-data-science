import sys

def ft_statistics(*args: any, **kwargs: any) -> None:
    if len(args) == 0 or kwargs is None:
        print("\033[1;31merror\033[0m !! args are empty !!")
        return
    # print(args, kwargs)
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
        if size == 0:
            print("\033[1;31merror\033[0m !!division by 0!!")
            return
        for num in nums:
            res += num
        return res / size


    def ft_quartile(nums):
        # METHOD 1 (“Inclusive”): Divide the data set into two halves, a bottom half and a top half. 
        # If n is odd, include the median value in both halves. Then the lower quartile is the median of the bottom half and the upper quartile is the median of
        # the top half. As an example, if S5 = (1, 2, 3, 4, 5), then the inclusive lower half is (1, 2, 3) and hence Q1 = 2. 
        """Calculate first and last quartile"""
        nums.sort()
        size = len(nums) / 2
        print(size)
        bottom = nums[0:int(size)]
        top = nums[int(size):-1]
        print(bottom, top)
        res = []
        res.append(bottom[-1:])
        res.append(top[-2:-1])
        return res
                    
    

    new_list = list(args)
    result = 0
    print(new_list)
    for word in kwargs.values():
        match word:
            case "median":
                result = ft_median(new_list)
            case "std":
                result = ft_std()
            case "var":
                result = ft_var(new_list)
            case "mean":
                result = ft_mean(new_list)
            case "quartile":
                result = ft_quartile(new_list)
            case _:
                return print("\033[1;31merror\033[0m !!key word not found!!")
        print(word, ":", result)
    

def main():
    pass
    #check args
    # ft_statistics(2, 1, 52, 4, 5, toto="median", maybe="quartile", var="var", std="std", mean="mean", _not="blabla")
    # ft_statistics(10, 2, 38, 23, 38, 21, 25, 26, 244, toto="mean")
    # ft_statistics(10, 2, 38, 23, 38, 21, 25, 26, 244, toto="median")
    # ft_statistics(555, 2, 10, 21, 23, 25, 26, 38, 38, 244, toto="var")
    # ft_statistics(2, 1, 52, 4, 5, var="var")
    
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, world="var")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")

    
    
if __name__ == "__main__":
    main()