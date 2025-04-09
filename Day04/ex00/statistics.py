import sys

def ft_statistics(*args: any, **kwargs: any) -> None:
    num_len = len(args)
    key_words = ["median", "std", "var", "mean", "quartile"]
   
    def ft_median():
        print("calling ft_median!")
    
    def ft_std():
        print("calling ft_std!")

    def ft_var():
        print("calling ft_var!")

    def ft_mean():
        print("calling ft_mean!")

    def ft_quartile():
        print("calling ft_quartile!")
    print("num_len:", num_len)
    print("arguments:", kwargs, "\n")
    for word in kwargs.values():
        match word:
            case "median":
                ft_median()
            case "std":
                ft_std()
            case "var":
                ft_var()    
            case "mean":
                ft_mean()
            case "quartile":
                ft_quartile()
            case _:
                print("key word not found")


    

def main():
    ft_statistics(1, 2, 3, 4, 5, toto="median", maybe="quartile", var="var", std="std", mean="mean", _not="blabla")
    
if __name__ == "__main__":
    main()