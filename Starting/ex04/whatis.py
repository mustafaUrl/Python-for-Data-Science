import sys

def isDigit(s):
    if s[0] == "-" or s[0] == "+":
        s = s[1:]
    for i in s:
        if not i.isdigit():
            return False
    return True
  

try:
    phrase = (sys.argv)
    print(len(phrase))
    if len(phrase) > 2:
        raise AssertionError("more than one argument is provided")
    if len(phrase) != 2:
        sys.exit()
    assert isDigit(phrase[1]), "argument is not a number"
    number = int(phrase[1]) 
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print("AssertionError:", e)