def ft_tqdm(lst: range) -> None:
    """Displays progress of iteration over lst with periodic yielding"""
    length = len(lst)
    bar_length = 50  # Length of the progress bar
    char = "█"
    for i in lst:
        percent = (i + 1) / length * 100  # Calculate percentage
        filled_length = int(bar_length * percent // 100)  # Calculate filled part of the bar
        
        # Build the bar string
        bar = char * filled_length + '-' * (bar_length - filled_length)
        
        # Display progress bar with percentage
        print(f"{int(percent)}% | [{bar}>] | {i+1}/{length}", end="\r")
        
        yield i  # Periodically yield values for the caller
    
   

