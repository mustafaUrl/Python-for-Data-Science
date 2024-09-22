def NULL_not_found(object: any) -> int:
    if type(object) == type(41) and not object:
        print("Zero:", object, type(object))
    elif type(object) == type("") and not object:
        print(f"Empty:{object} {type(object)}")
    elif type(object) == type(True) and not object:
        print("Fake:", object, type(object))
    elif not object:
        print("Nothing:", object, type(object))
    else:
        if type(object) == type(12.5) and object != object:
            print("Cheese:", object, type(object))
        else:
            print("Type not Found")
            return 1
    return 0