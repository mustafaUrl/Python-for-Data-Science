import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    '''
    
    '''
    try:
        if not family:
            raise Exception("Family must not be null.")
        if not isinstance(start, int):
            raise Exception("Start must not be an int.")
        if not isinstance(end, int):
            raise Exception("End must not be an int.")
        for elem in family:
            if not isinstance(elem, list):
                raise Exception("Family elements must be list.")
            for el in elem:
                if not(isinstance(el, float) or isinstance(el, int)):
                    raise Exception("list elements must be an int or a float")
        
        np_family = np.array(family)
        print("My shape is :",np_family.shape)
        new_np_arr = np_family[start:end]
        print("My new shape is :", new_np_arr.shape)
        return new_np_arr.tolist()
    except Exception as ex:
        print("Exception detected:", ex)
        return []