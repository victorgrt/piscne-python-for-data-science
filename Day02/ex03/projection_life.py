from load_csv import load


def projection_life():
    def draw_compare_data_set(dataset: pd.DataFrame):
    # NEED TO GET THE GOOD DATAS 

    # fr_data = dataset[dataset['country'] == 'France']
    # fr_years = fr_data.columns[1:].astype(float)
    # fr_population = convert_to_float(fr_data.values[0][1:])

    # jp_data = dataset[dataset['country'] == 'Belgium']
    # jp_years = jp_data.columns[1:].astype(float)
    # jp_population = convert_to_float(jp_data.values[0][1:])

    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['legend.loc'] = 'lower right'
    fig, ax = plt.subplots()

    # PROBABLY HAVE TO USE SCATTER
    # ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.plot(fr_years, fr_population, color='tab:red', label='France')
    plt.plot(jp_years, jp_population, color='tab:blue', label='Japan')
    ax.set_xlim(300, 10000)
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter)) 
    fig.canvas.manager.set_window_title('Compare Graph')
    plt.title('1900')
    
    plt.legend()
    plt.show()


def main():
    print("coucou")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    print(income)


if __name__ == "__main__":
    main()