import time
import os

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

r = f"{RED}"
g = f"{GREEN}"
cl = f"{RESET}"

c = "feliz"
b = "natal"

while True:
    os.system("cls")
    print(r, c, g, b)
    time.sleep(0.8)
    os.system("cls")
    print(g, c, r, b)
    time.sleep(0.8)