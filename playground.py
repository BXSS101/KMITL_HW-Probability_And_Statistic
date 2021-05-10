import matplotlib.pyplot as plt4
from statistics import mean
import csv
import time
import math

africa14, africa15, africa16 = [], [], []
america14, america15, america16 = [], [], []
asean14, asean15, asean16 = [], [], []
estasia14, estasia15, estasia16 = [], [], []
europe14, europe15, europe16 = [], [], []
mideast14, mideast15, mideast16 = [], [], []
oceania14, oceania15, oceania16 = [], [], []
soasia14, soasia15, soasia16 = [], [], []
path = 'c:/Users/akara/OneDrive - KMITL/Documents/GitHub/pythonFiles/Prob & Stat/thaitourism2.csv'

with open(path, 'r') as file:
    reader = csv.reader(file)
    #process for all year
    for row in reader:
        if row[0] == 'Africa' :
            africa14.append(int(row[2]))
            africa15.append(int(row[3]))
            africa16.append(int(row[4]))
        elif row[0] == 'Americas' :
            america14.append(int(row[2]))
            america15.append(int(row[3]))
            america16.append(int(row[4]))
        elif row[0] == 'ASEAN' :
            asean14.append(int(row[2]))
            asean15.append(int(row[3]))
            asean16.append(int(row[4]))
        elif row[0] == 'EstAsia' :
            estasia14.append(int(row[2]))
            estasia15.append(int(row[3]))
            estasia16.append(int(row[4]))
        elif row[0] == 'Europe' :
            europe14.append(int(row[2]))
            europe15.append(int(row[3]))
            europe16.append(int(row[4]))
        elif row[0] == 'MidEast' :
            europe14.append(int(row[2]))
            europe15.append(int(row[3]))
            europe16.append(int(row[4]))
        elif row[0] == 'Oceania' :
            oceania14.append(int(row[2]))
            oceania15.append(int(row[3]))
            oceania16.append(int(row[4]))
        elif row[0] == 'SoAsia' :
            soasia14.append(int(row[2]))
            soasia15.append(int(row[3]))
            soasia16.append(int(row[4]))

print("\tAfrica14 : " + "{:.2f}".format(round(mean(africa14), 2)))