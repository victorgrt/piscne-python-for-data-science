from load_csv import load

print(load.__doc__)
print(load("life_expectancy_years.csv"))
print("\n\n")

print("\033[31m# ERROR HANDLING #\033[0m")
load("bad_extension.csvv")
load("not_found.csv")
