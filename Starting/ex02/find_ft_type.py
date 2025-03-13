def all_thing_is_obj(object: any) -> int:
    """
    This function will print the type of the object passed in parameter
    :param object: any
    :return: int
    """
    types = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict"}

    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif types.get(type(object)) is not None:
        print(f"{types.get(type(object))} : {type(object)}")
    else:
        print("Type not found")
    return 42
