def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    '''
    
    '''
    try:
        if not height :
            raise Exception("Height must not be null")
        if not weight:
            raise Exception("Weight must not be null")
        for el1 in height:
            if not(isinstance(el1, float) or isinstance(el1, int)):
                raise Exception("Height array has a value which is not a float or an int.")
            if el1 < 0:
                raise Exception("Height Cannot be less than 0.")
            elif el1 == 0:
                raise ZeroDivisionError("0 division error detected.")
        for el2 in weight:
            if not(isinstance(el2, float) or isinstance(el2, int)):
                raise Exception("Weight array has a value which is not a float or an int.")
            if el2 < 0:
                raise Exception("Weight Cannot be less than 0.")
        if len(height) != len(weight):
            raise Exception("Height's length and Weight's length must be same.")
        ret_list = []
        for s in range(len(height)):
            ret_list.append(weight[s]/(height[s] ** 2))
        return ret_list
    except Exception as ex:
        print("Exception detected:", ex)
        return []





def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    
    
    '''
    try:
        if not bmi:
            raise Exception("Bmi must not be null")
        if not limit:
            raise Exception("Limit must not be null")
        for el1 in bmi:
            if el1 < 0:
                raise Exception("Bmi Cannot be less than 0.")
        ret_dict = []
        for s in range(len(bmi)):
            if bmi[s] > limit:
                ret_dict.append(True)
            else:
                ret_dict.append(False)
        return ret_dict

    except Exception as ex:
        print("Exception detected:", ex)
        return []
    
    