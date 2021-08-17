###################
# Disclaimer part #
###################
'''
HomeWork#3 | Probability Function
Course : Probability & Statistic
Instructor : Asst.prof. Surin Kittitornkun, Ph.D.
Semester / Academic Year : 2 / 2020
Institute : KMITL, Bangkok, Thailand
Developed By :  BXSS101 (Ackrawin B.)
Github URL : https://github.com/BXSS101
'''

################
# Program part #
################
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as pltA
import matplotlib.pyplot as pltB
import csv

lst14, lst15, lst16 = [], [], []
chklst14, chklst15, chklst16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0]
count = 0
#Start Program
print("============================================================")
print("============================================================")
print("    Welcome to thaitourism2.csv data processing program.")
print("============================================================")
#File Selecting
print("    Please Choose a File to Proceed . . . ")
print("        *leave it blank to use default file path")
print("Enter File Path : ", end='')
inPath = input()
'''
#select to display only year or year with months
print("        ↓↓↓ Select display mode to dispaly data ↓↓↓")
print("          \'A\' : Dispaly Month & Year")
print("          \'B\' : Dispaly only Year")
#check if input are in correct format
while True :
    mode = input("          SELECT MODE → ")
    if mode not in ('A', 'a', 'B', 'b', '') :
        print(" !!!!!!!! PLEASE TYPE ONLY A or B !!!!!!!!")
        print(" !!!!!!!!       INPUT AGAIN       !!!!!!!!")
    else :
        break
'''
print("============================================================")
print("============================================================")

#Open File and add Value to List
# 1 # C:/Users/akara/Documents/GitHub/pythonFiles/Prob & Stat/thaitourism2.csv
# 2 # C:/Users/HP/Documents/GitHub/pythonFiles/Prob & Stat/thaitourism2.csv
if inPath == '' :
    path = 'C:/Users/akara/Documents/GitHub/KMITL_HW-Probability_And_Statistic/thaitourism2.csv'
else :
    path = inPath
    
with open(path, 'r') as file:
    reader = csv.reader(file)
    #process for all year
    for row in reader:
        #sum all year
        if count >= 1 :
            lst14.append(int(row[2]))
            lst15.append(int(row[3]))
            lst16.append(int(row[4]))
            if int(row[2]) > 0 and int(row[2]) < 100001 :
                chklst14[0] = chklst14[0] + 1
            elif int(row[2]) > 100000 and int(row[2]) < 200001 :
                chklst14[1] = chklst14[1] + 1
            elif int(row[2]) > 200000 and int(row[2]) < 300001 :
                chklst14[2] = chklst14[2] + 1
            elif int(row[2]) > 300000 and int(row[2]) < 400001 :
                chklst14[3] = chklst14[3] + 1
            elif int(row[2]) > 400000 and int(row[2]) < 500001 :
                chklst14[4] = chklst14[4] + 1
            elif int(row[2]) > 500000 and int(row[2]) < 600001 :
                chklst14[5] = chklst14[5] + 1
            elif int(row[2]) > 600000 and int(row[2]) < 700001 :
                chklst14[6] = chklst14[6] + 1
            elif int(row[2]) > 900000 and int(row[2]) < 800001 :
                chklst14[7] = chklst14[7] + 1
            elif int(row[2]) > 800000 and int(row[2]) < 900001 :
                chklst14[8] = chklst14[8] + 1
            elif int(row[2]) > 900000 and int(row[2]) < 1000001 :
                chklst14[9] = chklst14[9] + 1
            elif int(row[2]) > 1000000 and int(row[2]) < 1100001 :
                chklst14[10] = chklst14[10] + 1
            elif int(row[2]) > 1100000 and int(row[2]) < 1200001 :
                chklst14[11] = chklst14[11] + 1
        count = count + 1

lst14.sort()
lst15.sort()
lst16.sort()
print(lst15)

#PDF Plot
pltA.plot(lst15,norm.pdf(lst15))
pltA.title('2015 Tourist PDF')
pltA.xlabel('Tourists (Million People)')
pltA.ylabel('Volume')
pltA.show()

pltA.plot(lst16,norm.pdf(lst16))
pltA.title('2016 Tourist PDF')
pltA.xlabel('Tourists (Million People)')
pltA.ylabel('Volume')
pltA.show()

#CDF Plot
values, base = np.histogram(lst15, bins = 96)
cumulative = np.cumsum(values)
pltB.plot(base[:-1], cumulative)
pltB.title('2015 Tourist CDF')
pltB.xlabel('Tourists (Million People)')
pltB.ylabel('Volume')
pltB.show()

values, base = np.histogram(lst16, bins = 96)
cumulative = np.cumsum(values)
pltB.plot(base[:-1], cumulative)
pltB.title('2016 Tourist CDF')
pltB.xlabel('Tourists (Million People)')
pltB.ylabel('Volume')
pltB.show()