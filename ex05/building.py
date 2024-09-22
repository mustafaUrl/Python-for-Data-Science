import sys


def take_input() -> str:
    '''
    Taking input when len(argv) is one
    '''
    print("What is the text to count?")
    ret = sys.stdin.read()
    print("")
    return ret


def print_values(ctrl):
    '''
    Printing values for output
    '''
    print(f"The text contains {len(ctrl)} characters:")
    upperCount, lowerCount, puncCount, spacesCount, digitsCount = 0, 0, 0, 0, 0
    for elem in ctrl:
        if elem.isupper():
            upperCount += 1
        elif elem.islower():
            lowerCount += 1
        elif elem in """!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~""":
            puncCount += 1
        elif elem.isspace() or elem == '\r':
            spacesCount += 1
        elif elem.isdigit():
            digitsCount += 1

    print(f"{upperCount} upper letters")
    print(f"{lowerCount} lower letters")
    print(f"{puncCount} punctuation marks")
    print(f"{spacesCount} spaces")
    print(f"{digitsCount} digits")


def main():
    """
    Main Function
    """
    try:
        args = sys.argv
        print(args, "*", len(args))
        ctrl = ""
        if len(args) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(args) == 1:
            ctrl = take_input()
        else:
            ctrl = args[1]
        print_values(ctrl=ctrl)
    except AssertionError as ex:
        print("AssertionError:", ex)


if __name__ == "__main__":
    main()
