import matplotlib.pyplot as plt
import numpy as np

info = {}
x = []
y = []

def read_file():
    file = open("f.dat", "r")
    for index, line in enumerate(file):
        fields = line.split(";")
        if index <= 28:
            info[fields[0]] = fields[1] + fields[2]
        else:
            x.append((float(fields[0].replace(',', '.'))))
            y.append((float(fields[1].replace(',', '.'))))
plt.plot(x, y)
plt.xscale('log')
plt.yticks(np.arange(min(y), max(y)+1, 1.0))
plt.show()
