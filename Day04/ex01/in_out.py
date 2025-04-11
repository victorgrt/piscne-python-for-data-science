def square(x:int | float) -> int | float:
    """RETUNRS SQUARE OF NUMBER."""
    return x * x
    
    
def pow(x:int | float) -> int | float:
    """RETURNS POWER OF NUMBER."""
    return x ** x
    
    
def outer(x: int | float, function) -> object:
    """CALLS FUNCTION(x) THEN RETURN THE VALUE.
    VALUE DEFINED AS NONLOCAL TO KEEP TRACK."""
    def inner() -> float:
        nonlocal x
        x = function(x)
        return x
    return inner
    
    
def main():
    pass


if __name__ == "__main__":
    main()