def give_bmi(height: list[int | float], weight: list[int | float]) ->\
      list[int | float]:
    '''Returns the BMI of the given height and weight
        BMI = weight / height^2
        If height and weight are empty, return empty list
        If height and weight are not empty, but length is
        not same, return empty list
        If any height or weight is less than or equal to 0, return empty list
        Else, return the BMI of each person in the list

    '''
    try:
        if len(height) != len(weight):
            raise AssertionError("Length of height and weight should be same")
        if not height or not weight:
            raise AssertionError("Height and weight should not be empty")
        if any(h <= 0 for h in height):
            raise AssertionError("Height should be greater than 0")
        if any(w <= 0 for w in weight):
            raise AssertionError("Weight should be greater than 0")
        bmi = [weight[i] / height[i] ** 2 for i in range(len(height))]
    except Exception as e:
        print("AssertionError: ", e)
        return []
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Returns the list of boolean values based on the limit
        If BMI is greater than the limit, then True else False'''
    try:
        if not bmi or not limit:
            raise AssertionError("BMI and limit should not be empty")
        if limit <= 0:
            raise AssertionError("Limit should be greater than 0")
        result = [b > limit for b in bmi]
    except Exception as e:
        print("AssertionError: ", e)
        return []
    return result
