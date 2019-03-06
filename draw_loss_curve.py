import matplotlib.pyplot as plt
import csv
import numpy as np


x = []
y = []

with open('training_loss.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(float(row[1]))
y = y[::-1]
x = x[::-1]
plt.plot(x,y)
plt.xlabel('Steps')
plt.ylabel('Loss')
plt.title('Steps vs Loss')
plt.show()