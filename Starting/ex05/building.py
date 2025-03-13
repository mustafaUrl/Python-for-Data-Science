import sys


def building(args):
    """Function to count the number of characters in a string"""
    (upper_letters, lower_letters, punctuation_marks, spaces, digits)\
        = [0, 0, 0, 0, 0]
    for j in args:
        if j.isupper():
            upper_letters += 1
        elif j.islower():
            lower_letters += 1
        elif j.isspace():
            spaces += 1
        elif j.isdigit():
            digits += 1
        elif j in [
            ".",
            ",",
            ":",
            ";",
            "!",
            "?",
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
            "'",
            '"',
            "-",
            "_",
            "/",
            "\\",
            "|",
            "@",
            "#",
            "$",
            "%",
            "&",
            "*",
            "+",
            "=",
            "<",
            ">",
            "~",
            "`",
            "^",
        ]:
            punctuation_marks += 1

    total = upper_letters + lower_letters + punctuation_marks + spaces + digits

    print(f"The text contains {total} characters:")
    print(upper_letters, "Uppercase letters: ")
    print(lower_letters, "Lowercase letters: ")
    print(punctuation_marks, "Punctuation marks: ")
    print(spaces, "Spaces: ")
    print(digits, "Digits: ")


def main():
    """Main function"""
    try:
        if len(sys.argv) < 2:
            try:
                print("What is the text to count?")
                text = sys.stdin.read()
            except KeyboardInterrupt:
                sys.exit(1)
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise ValueError("Too many arguments")
        building(text)

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    """Call the main function"""
    main()
    sys.exit(0)
