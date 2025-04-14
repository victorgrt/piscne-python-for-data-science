import sys

def ft_statistics(*args: any, **kwargs: any) -> None:
    if len(args) == 0 or kwargs is None:
        print("\033[1;31merror\033[0m !!args are empty!!")
        return
    # print(args, kwargs)
    num_len = len(args)
    key_words = ["median", "std", "var", "mean", "quartile"]
   
    def ft_median(nums):
        size = len(nums)
        sorted_nums = sorted(nums)  # Make sure the list is sorted
        mid = size // 2
        if size % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:
            return sorted_nums[mid]
    
    
    # \sigma=\sqrt{\dfrac{\sum{(x_i-\mu)^2}}{N}}
    # Step 1: Calculate the mean of the data—this is \mu in the formula
    # Step 2: Subtract the mean from each data point. These differences are called deviations. 
    # Data points below the mean will have negative deviations, and data points above the mean will have positive deviations.
    # Step 3: Square each deviation to make it positive.
    # Step 4: Add the squared deviations together.
    # Step 5: Divide the sum by the number of data points in the population. The result is called the variance.
    # Step 6: Take the square root of the variance to get the standard deviation.
    def ft_std(nums):
        res = ft_var(nums)
        return res ** 0.5
        
        

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
        nums_sorted = sorted(nums)
        size = len(nums_sorted)
        mid = size // 2

        # REAL QUARTILE CALCULATOR
        # if size % 2 == 0:
        #     lower_half = nums_sorted[:mid]
        #     upper_half = nums_sorted[mid:]
        # else:
        #     lower_half = nums_sorted[:mid]
        #     upper_half = nums_sorted[mid+1:]

        # q1 = ft_median(lower_half)
        # q3 = ft_median(upper_half)
        # return [q1, q3]
        # END
        
        if size % 2 == 0:
            lower_half = nums_sorted[:mid]
            upper_half = nums_sorted[mid:]
        else:
            lower_half = nums_sorted[:mid]
            upper_half = nums_sorted[mid+1:]
        
        q1 = lower_half[1:]
        q3 = upper_half[:-1]
        res = []
        res.append(float(*q1))
        res.append(float(*q3))

        return res

    new_list = list(args)
    result = 0
    for word in kwargs.values():
        match word:
            case "median":
                result = ft_median(new_list)
            case "std":
                result = ft_std(new_list)
            case "var":
                result = ft_var(new_list)
            case "mean":
                result = ft_mean(new_list)
            case "quartile":
                result = ft_quartile(new_list)
            case _:
                return print("\033[1;31merror\033[0m !!key word not found!!")
        print("\033[1m" + word + "\033[0m:", result)
    

def main():
    pass
    
    
if __name__ == "__main__":
    main()