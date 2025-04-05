from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def draw_data_set(dataset: pd.DataFrame):
    """
\033[1;33mdraw_data_set\033[0m:
- \033[33mNAME: draw_data_set\033[0m
- \033[34mARG: dataset\033[0m
- \033[35mRETURN VALUE: None\033[0m
\033[1;37mSelects data from a country then displays
it in a graph using matplotlib.\033[0m
    """
    france_data = dataset[dataset['country'] == 'France']
    print(france_data)
    years = france_data.columns[1:].astype(int)
    expectancy = france_data.values[0][1:]

    plt.rcParams['toolbar'] = 'None'
    fig, ax = plt.subplots()

    plt.xlabel("Year")
    plt.ylabel("Age")
    plt.plot(years, expectancy)
    ax.set_xlim(1800, 2100)
    fig.canvas.manager.set_window_title('🥖 FRANCE 🇫🇷')
    plt.title('France life expectancy Projections')
    plt.show()


def main():
    try:
        dataset = load("life_expectancy_years.csv")
    except AssertionError:
        return
    draw_data_set(dataset)


if __name__ == "__main__":
    main()
