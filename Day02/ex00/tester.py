from load_csv import load
import sys

print(load.__doc__)
print(load("life_expectancy_years.csv"))
print("\n\n")

print("\033[31m# ERROR HANDLING #\033[0m")
print(load("bad_extension.csvv"))
print(load("not_found.csv"))