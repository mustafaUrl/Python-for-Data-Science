import sys

def take_input() -> str:
    ret = input("What is the text to count?\n")
    #print(ret)
    return ret


def main():
    """
    Main Function
    """
    args = sys.argv
    print(args, "*", len(args))
    ctrl = ""
    if len(args) > 2:
        assert len(args) > 1, "more than one argument is provided"
    elif len(args) == 1:
        ctrl = take_input()
    else:
        ctrl = args[1]
    
    print(f"The text contains {len(ctrl)} characters:")
    upperCount,lowerCount, puncCount, spacesCount, digitsCount = 0,0,0,0,0
    for elem in ctrl:
        if elem.isupper():
            upperCount += 1
        elif elem.islower():
            lowerCount += 1
        elif elem in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            puncCount += 1
        elif elem.isspace():
            spacesCount += 1
        elif elem.isdigit():
            digitsCount += 1

    print(f"{upperCount} upper letters")
    print(f"{lowerCount} lower letters")
    print(f"{puncCount} punctuation marks")
    print(f"{spacesCount} spaces")
    print(f"{digitsCount} digits")
        


if __name__ == "__main__":
    main()
