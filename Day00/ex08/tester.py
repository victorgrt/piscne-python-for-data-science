from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print("\033[1;32m# DOCUMENTATION #\033[0m", end="")
print(ft_tqdm.__doc__)

print("\033[1;32m# NORMAL BEHAVIOR #")
sleep(1)
print("## ft_tqdm (mine) ##\033[0m")
sleep(1)

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

sleep(1)
print("\033[1;32m## tqdm (real) ##\033[0m")
sleep(1)
for elem in tqdm(range(333)):
    sleep(0.005)
print()

sleep(1)
print("\033[1;31m# ERROR HANDLING #\033[0m")
sleep(0.5)
for elem in ft_tqdm(range(-1)):
    sleep(0.005)
print()

sleep(0.5)
for elem in ft_tqdm(range(10000001)):
    sleep(0.005)
print()

sleep(0.5)
for elem in ft_tqdm("range??"):
    sleep(0.005)
print()

sleep(0.5)
for elem in ft_tqdm(list("coucou")):
    sleep(0.005)
print()
