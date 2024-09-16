from give_bmi import give_bmi, apply_limit

print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
print(give_bmi.__doc__)
print(apply_limit.__doc__)

print("\033[1;32m# BASIC TESTS #\033[0m")
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("\033[1;32m# ERROR HANDLING #\033[0m")
test = [None]
apply_limit(test, 26)
apply_limit(bmi, -1)
apply_limit(bmi, "test")
