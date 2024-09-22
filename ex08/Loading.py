def ft_tqdm(lst: range) -> None:
    BAR_SIZE = 100
    length = len(lst)
    for e in range(length+1):
        #print("")
        ret_str = ""
        num = int(e/length*100)
        beggining = f"{str(num).rjust(3)}%| "
        mid_block = BAR_SIZE*e//length - 1
        space_block = BAR_SIZE - mid_block - 1
        if BAR_SIZE*e//length == 0:
            space_block -= 1
        
        #print(mid_block, space_block, "*")
        mid="["
        for e1 in range(mid_block):
            mid += "="
        mid += ">"
        for e2 in range(space_block):
            mid += " "
        mid += "]"
        ending = f"| {e}/{length}"

        ret_str = beggining + mid +ending
        print(ret_str, end="\r")
        yield e

