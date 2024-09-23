def ft_filter(function, iter):
    '''
    takes each element in the iter and sends every element to the function and returns the ones that return true as an iter variable.
    '''
    if not function:
        return (x for x in iter if x)
    return (s for s in iter if function(s))
        