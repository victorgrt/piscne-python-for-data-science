from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def draw_data_set(dataset: pd.DataFrame):
    print("all good")
    # dataset.plot(x="test", y="test2", kind="bar")
    france_data = dataset[dataset['country'] == 'France']
    print(france_data)
    years = france_data.columns[1:].astype(int)
    expectancy = france_data.values[0][1:]
    print(type(years))
    print(type(expectancy))

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
    dataset = load("life_expectancy_years.csv")
    draw_data_set(dataset)
    # print(dataset.info())


if __name__ == "__main__":
    main()