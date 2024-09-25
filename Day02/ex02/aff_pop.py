from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def convert_to_float(population_data):
    return [float(x.replace('M', '')) for x in population_data]


def millions_formatter(x, pos):
    return f'{x}M'


def draw_compare_data_set(dataset: pd.DataFrame):
    fr_data = dataset[dataset['country'] == 'France']
    fr_years = fr_data.columns[1:].astype(float)
    fr_population = convert_to_float(fr_data.values[0][1:])

    jp_data = dataset[dataset['country'] == 'Belgium']
    jp_years = jp_data.columns[1:].astype(float)
    jp_population = convert_to_float(jp_data.values[0][1:])

    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['legend.loc'] = 'lower right'
    fig, ax = plt.subplots()
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.plot(fr_years, fr_population, color='tab:red', label='France')
    plt.plot(jp_years, jp_population, color='tab:blue', label='Japan')
    ax.set_xlim(1800, 2050)
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter)) 
    fig.canvas.manager.set_window_title('Compare Graph')
    plt.title('Population Projections')
    
    plt.legend()
    plt.show()


def main():
    dataset = load("population_total.csv")
    draw_compare_data_set(dataset)

if __name__ == "__main__":
    main()