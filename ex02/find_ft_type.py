def all_thing_is_obj(object: any) -> int:
    if (type(object) == type(["xd"])):
        print("List :", type(object))
    elif (type(object) == type(("xd","yo"))):
        print("Tuple :", type(object))
    elif (type(object) == type({"xd", "xd"})):
        print("Set :", type(object))
    elif(type(object) == type({"xd":"xd"})):
        print("Dict :", type(object))
    elif(type(object) == type("")):
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")
    return 42
