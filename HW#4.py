###################
# Disclaimer part #
###################
'''
HomeWork#4 | Probability Function
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
from matplotlib import pyplot as pltA
import seaborn as sns
import numpy as np
import csv

lst16 = []
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
            lst16.append(int(row[4]))
        count = count + 1

lst16.sort()
#print(lst16)
#print(len(lst16))
#data
#x = np.array(lst16)
x = list(range(1, 97))
y = np.array(lst16)

fig, ax = pltA.subplots()
ax = sns.lineplot(x, y, ci = 99)
pltA.title('2016 Tourists CI')
pltA.ylabel('Amount of Tourist (Million People)')
pltA.show()