from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def aff_life(country: str):
    """
    This function takes a country name as input and returns a plot of life
    expectancy over the years for that country.
    """
    data = load('../life_expectancy_years.csv')
    country_data = data.loc[country]
    print(country_data)
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('Life expectancy in ' + country)
    country_data.index = country_data.index.astype(int)
    # alt satırı kontrol et
    country_data = country_data.astype(int)
    plt.xticks(np.arange(min(country_data.index),
                         max(country_data.index)+1, 40))
    plt.plot(country_data.index, country_data)
    plt.show()
    # return df['Life expectancy'] / df['GDP per capita']


aff_life('Turkey')
