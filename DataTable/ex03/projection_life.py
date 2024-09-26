import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def main():
    df_gdp = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_expectancy = load("../life_expectancy_years.csv")
    
    gdp = df_gdp['1900']  
    expectancy = df_expectancy['1900']
    
    plt.scatter(gdp, expectancy)

    plt.title("1900")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Eexpectancy")
    plt.xscale('log')

    ticks = [300, 1000, 10000]  # Positions of ticks
    tick_labels = ['300', '1k', '10k']  # Custom labels

    plt.xticks(ticks, tick_labels)  # Set custom ticks and labels

    plt.show()

# Çalıştırmak için main fonksiyonunu çağırıyoruz
if __name__ == "__main__":
    main()


# import pandas as pd
# from load_csv import load
# import matplotlib.pyplot as plt
# import numpy as np



# def main():
#     df_gdp = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
#     df_expectancy = load("../life_expectancy_years.csv")
    
#     gdp = df_gdp.loc['1900']  
#     gdp.index = gdp.index.astype(int)
  
 
#     expectancy = df_expectancy.loc['1900']
#     expectancy.index = expectancy.index.astype(int)


    

#     plt.legend()
#     plt.show()

# if __name__ == "__main__":
#     main()
