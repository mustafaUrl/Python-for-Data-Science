


def ft_mean(*args: any) -> float:
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


def ft_median(*args: any) -> float:
    if len(args) == 0:
        return 0
    args = sorted(args)
    if len(args) % 2 == 0:
        return (args[len(args) // 2 - 1] + args[len(args) // 2]) / 2
    return args[len(args) // 2]

   

def percentile(data, percentile):
    
   
    index = (percentile / 100) * (len(data) - 1)  # Yüzdeye göre indeksi hesapla
    lower_index = int(index)  # Alt indeks
    upper_index = lower_index + 1  # Üst indeks

    if upper_index >= len(data):  # Eğer üst indeks veri uzunluğunu aşarsa
        return data[lower_index]

    # Aradaki değeri hesapla
    weight = index - lower_index
    return data[lower_index] * (1 - weight) + data[upper_index] * weight

def ft_quartile(*args: float):
    """ Calculate Q1 and Q3 like NumPy and SciPy. """
    
    if len(args) == 0:
        return (0.0, 0.0)
    sorted_data = sorted(float(arg) for arg in args)
    Q1 = percentile(sorted_data, 25)
    Q3 = percentile(sorted_data, 75)
    return (Q1, Q3)




  






def ft_std(*args: any) -> float:
    if len(args) == 0:
        return 0,
    return ft_var(*args) ** 0.5
    # mean = ft_mean(*args)
    # return (sum((i - mean) ** 2 for i in args) / len(args)) ** 0.5


def ft_var(*args: any) -> float:
    if len(args) == 0:
        return 0
    mean = ft_mean(*args)
    return sum((i - mean) ** 2 for i in args) / len(args)



def ft_statistics(*args: any, **kwargs: any) -> None:
    check_list = ["mean", "median", "quartile", "std", "var"]
    key_list = list(kwargs.values())
    for i in key_list:
        if i not in check_list:
            return 
    for key, value in kwargs.items():
        if value == "mean" and not len(args) == 0:
            print(f"{key}: {ft_mean(*args)}")
        elif value == "median" and not len(args) == 0:
            print(f"{key}: {ft_median(*args)}")
        elif value == "quartile" and not len(args) == 0:
            print(f"{key}: {ft_quartile(*args)}")
        elif value == "std" and not len(args) == 0:
            print(f"std: {ft_std(*args)}")
        elif value == "var" and not len(args) == 0:
            print(f"var: {ft_var(*args)}")
        else:
            print("ERROR")