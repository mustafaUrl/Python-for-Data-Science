import math

def NULL_not_found(object: any) -> int:
    types = { float: "Cheese: nan", int : "Zero: 0",\
    str : "Empty:", bool : "Fake: False"}


lambda
    # var_null =  { float:  , int : "Zero: 0",\
    # str : "Empty:", bool : "Fake: False"}
    if type(object) == type(None):
        print( f"Nothing : {type(object)}")
    elif types.get(type(object)) != None:
        print( f"{types.get(type(object))} {type(object)}")
    else:
        print("Type not found")
        return 1
    
    return 0
