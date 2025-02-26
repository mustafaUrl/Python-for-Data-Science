from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def toNum(value):
    """
    Convert a string to a number.
    """

    if value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    elif value.endswith('k'):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def main():
    """
    Load the population data for Turkey and France and
    plot the population projections.
    """

    df = load("../population_total.csv")
    # Processing data for Turkey
    # Assuming you meant 'Turkey' instead of 'Belgium'
    turkey = df.loc['Belgium']
    turkey.index = turkey.index.astype(int)
    turkey = turkey[(turkey.index >= 1800) & (turkey.index <= 2050)]
    turkey = turkey.apply(toNum)
    # Processing data for France
    france = df.loc['France']
    france.index = france.index.astype(int)
    france = france[(france.index >= 1800) & (france.index <= 2050)]
    france = france.apply(toNum)
    years = france.index
    # Set labels and title
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    # Get the maximum population value from both countries
    max_population = max(turkey.max(), france.max())
    # Define y-axis ticks, round the max_population to the nearest 20 million
    y_max = np.ceil(max_population / 20_000_000) * 20_000_000
    y_ticks = np.arange(0, y_max + 1, 20_000_000)
    plt.yticks(y_ticks, [f"{int(i // 1_000_000)}M" for i in y_ticks])
    # Plot Turkey and France population data
    plt.plot(years, turkey, label='Turkey')
    plt.plot(years, france, label='France')
    # Display legend and plot
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
