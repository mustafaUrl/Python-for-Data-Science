import sys
from ft_filter import ft_filter


def isNum(num) -> bool:
    """
    Checking the string is a number
    """
    if num == "" or num == "''" or not len(num):
        return False
    lst = list(num)
    if lst[0] == '+' or lst[0] == '-':
        lst = lst[1:]
    for digit in lst:
        if not digit.isdigit():
            return False
    return True
    '''
    def control(x, num) -> bool:
        print(x)
        if len(x) > num:
            return True
        return False
    '''
    


def main():
    """
    Main Function
    Output is a list of the iters return from ft_filter
    """

    try:
        args = sys.argv
        assert len(args) == 3, "the arguments are bad"
        try:
            assert isNum(args[2]), "the arguments are bad"
            int(args[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(list(ft_filter(lambda x: len(x) > int(args[2]),
              sys.argv[1].split(' '))))
    except AssertionError as ex:
        print("AssertionError", ex)


if __name__ == "__main__":
    main()
