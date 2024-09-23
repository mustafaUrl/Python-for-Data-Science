import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    '''This function takes a list of lists and two integers as input.
        It returns a list of lists that is a slice of the input list of lists.
         The slice starts at the index start and ends at the index end. 
         The input list of lists is a 2D array. The function returns 
         an empty list if the input is invalid. The function returns 
         the slice of the input list of lists if the input is valid'''
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Start and end must be integers")
        if not isinstance(family, list):
            raise AssertionError("Family must be a list")
        if not all(isinstance(i, list) for i in family):
            raise AssertionError("Family must be a list of lists")
               
        family = np.array(family)

        print("My shape is :", family.shape)
        family = family[start:end]
        print("My new shape is :", family.shape)
        list_family = family.tolist()
        return list_family
    except Exception as e:
        print("Error: ", e)
        return []
    
    