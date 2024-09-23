from ft_filter import ft_filter
import sys

def main():
    '''Main function'''
    try:
        if len(sys.argv) != 3:
            raise AssertionError("The arguments are bad")
        
        try:
            strVal = sys.argv[1].split(' ')  # Split input string into a list
            intVal = int(sys.argv[2])
        except ValueError:
            raise AssertionError("The arguments are bad")


        # Use a lambda function to filter based on the length condition
        filtered = list(ft_filter(lambda item: len(item) > intVal, strVal))
        
        print(filtered)

    except Exception as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
