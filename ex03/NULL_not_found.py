def NULL_not_found(object: any) -> int:
    types = { float: "Cheese: nan", int : "Zero: 0",\
    str : "Empty:", bool : "Fake: False"}

    check = { float: float("NaN"), int : 0,\
    str : "", bool : False}
  



    if type(object) == type(None):
        print( f"Nothing : None {type(object)}")
    elif type(object) == float and object != object:  # NaN kontrolü
        print(f"{types.get(float)} {type(object)}")
    elif types.get(type(object)) != None and  object == check.get(type(object)) :
        print( f"{types.get(type(object))} {type(object)}")
    else:
        print("Type not Found")
        return 1
    
    return 0
