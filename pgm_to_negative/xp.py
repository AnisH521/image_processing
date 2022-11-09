import numpy as np

with open("dog.pgm", "r") as f:
    a = f.readline()
    b = f.readline()
    c = f.readline()
    max = f.readline()

    f.close()

col, row = [int(i) for i in c.split()]

with open("dog3.pgm", "w") as f:
    f.close()