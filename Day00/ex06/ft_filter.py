def ft_filter(func, iterable):
    if func:
        return (item for item in iterable if func(item))
    return (item for item in iterable if item)
