from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def draw_compare_data_set(dataset: pd.DataFrame):
    print("all good")
    france_data = dataset[dataset['country'] == 'France']
    print(france_data)
    years = france_data.columns[1:].astype(int)
    population = france_data.values[0][1:]

    plt.rcParams['toolbar'] = 'None'
    fig, ax = plt.subplots()

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.plot(years, color='tab:orange')
    plt.plot(population, color='tab:orange')
    ax.set_xlim(1800, 2050) 
    fig.canvas.manager.set_window_title('Compare Graph')
    plt.title('Population Projections')
    plt.show()

def main():
    dataset = load("population_total.csv")
    draw_compare_data_set(dataset)

if __name__ == "__main__":
    main()