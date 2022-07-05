import matplotlib.pyplot as plt
import numpy as np

#1. generation
iter_num = 100
start_random = 1
adder = 0
multiplier = 10
modulo = 7
psudo_list = []
for i in range(iter_num):
    if i == 0:
        psudo_list.append(np.mod(start_random * multiplier + adder, modulo ))
    else:
        psudo_list.append(np.mod(psudo_list[i-1] * multiplier + adder, modulo ))



#2. graph generate
print(psudo_list)
plt.plot(psudo_list)
plt.show()