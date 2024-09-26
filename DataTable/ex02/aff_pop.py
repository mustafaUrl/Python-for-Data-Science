from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def main(country1: str, country2: str, file: str):

    data = load(file)
    country1_data = data.loc[country1]
    country2_data = data.loc[country2]


    plt.xlabel('Population') 
    plt.ylabel('Year')
    plt.title('Population in ' + country1 + ' and ' + country2)
    country_data.index = country_data.index.astype(int)
    contry_data = country_data.astype(int)
    plt.xticks(np.arange(min(country_data.index), max(country_data.index)+1, 40))

    plt.plot(country_data.index, country_data)
    plt.show()


if __name__ == '__main__':
    main('Turkey','France','../life_expectancy_years.csv')