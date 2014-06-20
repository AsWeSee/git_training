import sys
import random
from massiv import *

print(sys.argv)

mas = []
for x in range(10):
    mas.append(x*x)
    if mas[x] % 2 == 0:
        print(x,mas[x])

print_mas(block[0],block[1])
