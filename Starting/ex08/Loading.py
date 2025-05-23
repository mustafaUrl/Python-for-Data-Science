import os


def get_terminal_width():
    """ Get the terminal width using the os library"""

    return os.get_terminal_size().columns


def ft_tqdm(lst: range) -> None:
    """Displays progress of iteration over lst with periodic yielding"""

    length = len(lst)
    terminal_width = get_terminal_width()
    bar_length = terminal_width - 30
    char = "█"
    for i in lst:
        percent = (i + 1) / length * 100
        filled_length = int(bar_length * percent // 100)
        bar = char * filled_length + ' ' * (bar_length - filled_length)
        print(f"{int(percent)}% | [{bar}>] | {i+1}/{length}", end="\r")
        yield i
