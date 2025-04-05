from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def projection_life(income: pd.DataFrame, life: pd.DataFrame,
                    year: str = "1900"):
    """Plot GDP per capita vs. life expectancy for a given year."""
    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['legend.loc'] = 'lower right'

    income.set_index("country", inplace=True)
    life.set_index("country", inplace=True)

    income[year] = pd.to_numeric(income[year], errors='coerce')
    life[year] = pd.to_numeric(life[year], errors='coerce')

    plt.figure(figsize=(8, 6))
    plt.scatter(income[year], life[year], alpha=0.7, edgecolors="k")

    plt.xlabel("Gross Domestic Product (GDP per capita)")
    plt.ylabel("Life Expectancy (years)")

    plt.title('Life Expectancy vs GDP in 1900')
    plt.show()


def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    projection_life(income, life, year="1900")


if __name__ == "__main__":
    main()
