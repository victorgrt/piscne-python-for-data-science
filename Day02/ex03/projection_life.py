from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def projection_life(income: pd.DataFrame, life: pd.DataFrame, year: str = "1900"):
    """Plot GDP per capita vs. life expectancy for a given year."""
    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['legend.loc'] = 'lower right'


    # Ensure 'country' is used as an index
    income.set_index("country", inplace=True)
    life.set_index("country", inplace=True)

    # Convert the year column to numeric (in case of string format)
    income[year] = pd.to_numeric(income[year], errors='coerce')
    life[year] = pd.to_numeric(life[year], errors='coerce')

    # Drop rows with missing values
    data = pd.DataFrame({
        "GDP": income[year],
        "Life Expectancy": life[year]
    }).dropna()

    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(data["GDP"], data["Life Expectancy"], alpha=0.7, edgecolors="k")

    plt.xlabel("Gross Domestic Product (GDP per capita)")
    plt.ylabel("Life Expectancy (years)")

    plt.title('Life Expectancy vs GDP in 1900')
    plt.show()


# def projection_life(income: pd.DataFrame, life: pd.DataFrame):

#     plt.rcParams['toolbar'] = 'None'
#     plt.rcParams['legend.loc'] = 'lower right'
#     fig, ax = plt.subplots()

#     plt.xlabel("Gross domestic product")
#     plt.ylabel("Life Expectancy")
#     ax.set_xlim(300, 10000)
#     fig.canvas.manager.set_window_title('Compare Graph')
#     plt.title('1900')
    
#     plt.legend()
#     plt.show()


def main():
    print("coucou")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    print(income)
    print(life)
    projection_life(income, life, year="1900")

if __name__ == "__main__":
    main()