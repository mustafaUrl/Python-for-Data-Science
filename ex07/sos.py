import sys

def GET_NESTED_MORSE(message):
    '''Get the nested morse code'''
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
    return NESTED_MORSE.get(message.upper(), "")

def check_sos(message):
    '''Check if the message is SOS'''
    if len(message) == 0:
        return False
    for i in message:
        if i.isalnum() or i.isspace():
            continue
        return False
    return True


def main():
    '''Main function'''
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the number of arguments is bad")
        message = sys.argv[1]
        if not check_sos(message):
            raise AssertionError("the arguments are bad")
        morse_message = ""
        for i in message:
            morse_message += GET_NESTED_MORSE(i)
        print(morse_message)

    except Exception as e:
        print("AssertionError: ", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)