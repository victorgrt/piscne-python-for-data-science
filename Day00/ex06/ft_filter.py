def ft_filter(func, iterable):
    """
\033[1;33mft_filter\033[0m:
    - \033[33mNAME: ft_filter\033[0m
    - \033[34mARG: function, list\033[0m
    - \033[35mRETURN VALUE: new list\033[0m
\033[1;37m- Using a list comprehension, filters the list given keeping only\
the elements that function(elem) is True.\033[0m
    """
    if func:
        return (item for item in iterable if func(item))
    return (item for item in iterable if item)
