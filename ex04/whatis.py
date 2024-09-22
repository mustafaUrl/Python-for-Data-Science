import sys


def isNum(num):
    if num == "" or num == "''" or not len(num):
        return False
    lst = list(num)
    if lst[0] == '+' or lst[0] == '-':
        lst = lst[1:]
    for digit in lst:
        if not digit.isdigit():
            return False
    return True


try:
    argvs = sys.argv
    if (len(argvs) == 1):
        sys.exit()
    elif (len(argvs) != 2):
        raise AssertionError("more than one argument is provided")
    try:
        '''
        if not argvs[1].isdigit():
            raise AssertionError("argument is not an integer")
        '''
        assert isNum(argvs[1]), "argument is not an integer"
        int(argvs[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    print("I'm Odd.") if int(argvs[1]) else print("I'm Even.")

except AssertionError as ex:
    print("AssertionError:", ex)
