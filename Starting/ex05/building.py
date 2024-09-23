import sys



def building(args):
    '''Function to count the number of characters in a string'''
    (upper_letters , lower_letters,\
    punctuation_marks, spaces, digits) = [0, 0, 0, 0, 0]
    for j in args:
        if j.isupper():
            upper_letters += 1
        elif j.islower():
            lower_letters += 1
        elif j.isspace() or j == "\r" or j == "\r\n":
            spaces += 1
        elif j.isdigit():
            digits += 1
        elif j in [".", ",", ":", ";", "!", "?", "(", ")", \
        "[", "]", "{", "}", "'", '"', "-", "_", "/", "\\",\
         "|", "@", "#", "$", "%", "&", "*", "+", "=", "<", ">", "~", "`", "^"]:
            punctuation_marks += 1

    total = (upper_letters + lower_letters + punctuation_marks + spaces + digits)


    print(f"The text contains {total} characters:")
    print(upper_letters, "Uppercase letters: ")
    print(lower_letters, "Lowercase letters: ",)
    print(punctuation_marks, "Punctuation marks: ")
    print(spaces, "Spaces: ")
    print(digits, "Digits: ")






def main():
    '''Main function'''
    if len(sys.argv) < 2:
        # text = input("What is the text to count?\n")
        try:
            text = sys.stdin.read()
            print("What is the text to count?")
        except KeyboardInterrupt:
            sys.exit(1)
    elif len(sys.argv) > 2:
        raise ValueError("Too many arguments")
    else:
        text = sys.argv[1]
    try:
        building(text)
        
    except Exception as e:
        print(e)
        sys.exit(1)



if __name__ == "__main__":
    main()
    sys.exit(0)
