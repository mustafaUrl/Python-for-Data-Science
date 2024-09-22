import sys 

def string_control(str_) -> bool:
    '''
    Controlling the string and checking is there any character is not a alphanumeric or space
    '''
    for el in str_:
        if not (el.isalnum() or el.isspace()):
            return False
    return True

def str_to_morse(str_) -> str:
    '''
    Get the string and convert it to morse with using  NESTED_MORSE dict variable
    '''
    NESTED_MORSE = { " ": "/",
                         "A": ".-",
                         'B':'-...',
                         'C':'-.-.',
                         'D':'-..',
                         'E':'.',
                         'F':'..-.',
                         'G':'--.',
                         'H':'....',
                         'I':'..',
                         'J':'.---',
                         'K':'-.-',
                         'L':'.-..',
                         'M':'--',
                         'N':'-.',
                         'O':'---',
                         'P':'.--.',
                         'Q':'--.-',
                         'R':'.-.',
                         'S':'...',
                         'T':'-',
                         'U':'..-',
                         'V':'...-',
                         'W':'.--',
                         'X':'-..-',
                         'Y':'-.--',
                         'Z':'--..',
                         '1':'.----',
                         '2':'..---',
                         '3':'...--',
                         '4':'....-',
                         '5':'.....',
                         '6':'-....',
                         '7':'--...',
                         '8':'---..',
                         '9':'----.',
                         '0':'-----',
        }

    ret_str = ""
    for e in str_:
        ret_str += NESTED_MORSE[e.upper()] + " "
    return ret_str[:-1]


def main():
    '''
    Main Function
    '''
    try:
        args = sys.argv
        #print(args)
        assert len(args) == 2, "the arguments are bad"
        assert string_control(args[1]), "the arguments are bad"
        print(str_to_morse(args[1]))

    except AssertionError as ex:
        print(ex)


if __name__ == "__main__":
    main()