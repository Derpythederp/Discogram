# Discogram-Histogram but better
import numpy as np
import matplotlib.pyplot as plt
import random

filename3 = "assets/coe-results.csv"
data3 = np.genfromtxt(filename3, dtype=['U10', 'i2', 'U20', 'i4', 'i4', 'i4','i4'], 
                     delimiter=',', names=True)
range_prem= data3['premium']

while True:
    num_bins= random.randint(5,25)
    n, bins, patches= plt.hist(range_prem, num_bins)
    plt.xlabel("Number of vehicles")
    plt.ylabel("Premium")
    patchcolor= ['b','g','r','c','m','y','k']

    for i in range(len(patches)):
        color=patchcolor[random.randrange(len(patchcolor))]
        plt.setp(patches[i], 'facecolor', color)
        
    plt.show() #discogram- for the people who like second glances at their data in a new (albeit flashing) light
    plt.savefig("Party")

