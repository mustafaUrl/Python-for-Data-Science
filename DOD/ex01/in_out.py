def square(x: int | float) -> int | float:
    """Return the square of the input."""
    x = x ** 2
    return x

def pow(x: int | float) -> int | float:
    """Return the power of the input."""
    x = x ** x
    return x
    
def outer(x: int | float, function) -> object:
    """Return a function that applies the input function to the input value."""
    count = 0
    def inner() -> float:
        nonlocal count, x
        count += 1
        x = function(x)
        return  x
    return inner


