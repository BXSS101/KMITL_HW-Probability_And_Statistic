###################
# Disclaimer part #
###################
'''
HomeWork#2 | Plot & Basic Statistic
Course : Probability & Statistic
Instructor : Asst.prof. Surin Kittitornkun, Ph.D.
Semester / Academic Year : 2 / 2020
Institute : KMITL, Bangkok, Thailand
Developed By :  BXSS101 (Ackrawin B.)
Github URL : https://github.com/BXSS101
'''

#################
# Notes & To Do #
#################
"""
:: To Do ::
√Add feature choose display month or not
√Add delay for easier reading
√Add list to check each month
 Add dictionary for region
√Add interface
 Add more fancy interface
ื√Add Graph : Histogram, Box plot, Stem, Leaf
√Add File path selecting Function
√Add Comment to Expalin code
"""

################
# Program part #
################
import matplotlib.pyplot as pltA     #For Graph plotting
import matplotlib.pyplot as pltB
import matplotlib.pyplot as plt0
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
from statistics import mean         #For find mean from int list
import csv                          #For Reading CSV Files
import time                         #For Delay setting
import math                         #For math calculation : sqrt

#Function to find Average/Mean from 'string' list
def findAvg(inLst) :
    sumOfLst = 0
    for i in inLst : sumOfLst = sumOfLst + int(i)
    return sumOfLst/len(inLst)

#Function fo find Standard Deviation (S.D.) from 'string' list
def findSD(inLst) :
    tempPowSum = 0
    tempSumPow = 0
    for i in inLst :
        tempPowSum = tempPowSum + pow(int(i), 2)
        tempSumPow = tempSumPow + int(i)
    return math.sqrt(((len(inLst) * tempPowSum) - pow(tempSumPow, 2)) / (len(inLst) * (len(inLst) - 1)))

#variable for count rows & sum of each year
count, sum14, sum15, sum16 = 0, 0, 0, 0
#list for store value each year/month
lst14, lst0114, lst0214, lst0314, lst0414, lst0514, lst0614, lst0714, lst0814, lst0914, lst1014, lst1114, lst1214 = [], [], [], [], [], [], [], [], [], [], [], [], []
lst15, lst0115, lst0215, lst0315, lst0415, lst0515, lst0615, lst0715, lst0815, lst0915, lst1015, lst1115, lst1215 = [], [], [], [], [], [], [], [], [], [], [], [], []
lst16, lst0116, lst0216, lst0316, lst0416, lst0516, lst0616, lst0716, lst0816, lst0916, lst1016, lst1116, lst1216 = [], [], [], [], [], [], [], [], [], [], [], [], []
lst14E, lst15E, lst16E = [int(0) for va in range(0,12)], [int(0) for va in range(0,12)], [int(0) for va in range(0,12)]
#dict for store region
regDict14 = {'Africa' : [], 'Americas' : [], 'ASEAN' : [], 'EstAsia' : [], 'Europe' : [], 'MidEast' : [], 'Oceania' : [], 'SoAsia' : []}
regDict15 = {'Africa' : [], 'Americas' : [], 'ASEAN' : [], 'EstAsia' : [], 'Europe' : [], 'MidEast' : [], 'Oceania' : [], 'SoAsia' : []}
regDict16 = {'Africa' : [], 'Americas' : [], 'ASEAN' : [], 'EstAsia' : [], 'Europe' : [], 'MidEast' : [], 'Oceania' : [], 'SoAsia' : []}

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
            sum14 = sum14 + int(row[2])
            sum15 = sum15 + int(row[3])
            sum16 = sum16 + int(row[4])

            lst14.append(int(row[2]))
            lst15.append(int(row[3]))
            lst16.append(int(row[4]))
            if row[1] == '1' :
                lst0114.append(int(row[2]))
                lst0115.append(int(row[3]))
                lst0116.append(int(row[4]))
                lst14E[0] = lst14E[0] + int(row[2])
                lst15E[0] = lst15E[0] + int(row[3])
                lst16E[0] = lst16E[0] + int(row[4])
            elif row[1] == '2' :
                lst0214.append(int(row[2]))
                lst0215.append(int(row[3]))
                lst0216.append(int(row[4]))
                lst14E[1] = lst14E[1] + int(row[2])
                lst15E[1] = lst15E[1] + int(row[3])
                lst16E[1] = lst16E[1] + int(row[4])
            elif row[1] == '3' :
                lst0314.append(int(row[2]))
                lst0315.append(int(row[3]))
                lst0316.append(int(row[4]))
                lst14E[2] = lst14E[2] + int(row[2])
                lst15E[2] = lst15E[2] + int(row[3])
                lst16E[2] = lst16E[2] + int(row[4])
            elif row[1] == '4' :
                lst0414.append(int(row[2]))
                lst0415.append(int(row[3]))
                lst0416.append(int(row[4]))
                lst14E[3] = lst14E[3] + int(row[2])
                lst15E[3] = lst15E[3] + int(row[3])
                lst16E[3] = lst16E[3] + int(row[4])
            elif row[1] == '5' :
                lst0514.append(int(row[2]))
                lst0515.append(int(row[3]))
                lst0516.append(int(row[4]))
                lst14E[4] = lst14E[4] + int(row[2])
                lst15E[4] = lst15E[4] + int(row[3])
                lst16E[4] = lst16E[4] + int(row[4])
            elif row[1] == '6' :
                lst0614.append(int(row[2]))
                lst0615.append(int(row[3]))
                lst0616.append(int(row[4]))
                lst14E[5] = lst14E[5] + int(row[2])
                lst15E[5] = lst15E[5] + int(row[3])
                lst16E[5] = lst16E[5] + int(row[4])
            elif row[1] == '7' :
                lst0714.append(int(row[2]))
                lst0715.append(int(row[3]))
                lst0716.append(int(row[4]))
                lst14E[6] = lst14E[6] + int(row[2])
                lst15E[6] = lst15E[6] + int(row[3])
                lst16E[6] = lst16E[6] + int(row[4])
            elif row[1] == '8' :
                lst0814.append(int(row[2]))
                lst0815.append(int(row[3]))
                lst0816.append(int(row[4]))
                lst14E[7] = lst14E[7] + int(row[2])
                lst15E[7] = lst15E[7] + int(row[3])
                lst16E[7] = lst16E[7] + int(row[4])
            elif row[1] == '9' :
                lst0914.append(int(row[2]))
                lst0915.append(int(row[3]))
                lst0916.append(int(row[4]))
                lst14E[8] = lst14E[8] + int(row[2])
                lst15E[8] = lst15E[8] + int(row[3])
                lst16E[8] = lst16E[8] + int(row[4])
            elif row[1] == '10' :
                lst1014.append(int(row[2]))
                lst1015.append(int(row[3]))
                lst1016.append(int(row[4]))
                lst14E[9] = lst14E[9] + int(row[2])
                lst15E[9] = lst15E[9] + int(row[3])
                lst16E[9] = lst16E[9] + int(row[4])
            elif row[1] == '11' :
                lst1114.append(int(row[2]))
                lst1115.append(int(row[3]))
                lst1116.append(int(row[4]))
                lst14E[10] = lst14E[10] + int(row[2])
                lst15E[10] = lst15E[10] + int(row[3])
                lst16E[10] = lst16E[10] + int(row[4])
            elif row[1] == '12' :
                lst1214.append(int(row[2]))
                lst1215.append(int(row[3]))
                lst1216.append(int(row[4]))
                lst14E[11] = lst14E[11] + int(row[2])
                lst15E[11] = lst15E[11] + int(row[3])
                lst16E[11] = lst16E[11] + int(row[4])
        #counter
        count = count + 1

if True :  # Draw ::::
    #print("Row count = " + str(count), end='\n\n')
    time.sleep(0.5)
    print(":::::")
    time.sleep(0.4)
    print("::::")
    time.sleep(0.3)
    print(":::")
    time.sleep(0.2)
    print("::")
    time.sleep(0.1)
    print(":")

#Dispaly Mean Section
print(" ///// MEAN FROM ALL REGION EACH MONTH FROM 2014 - 2016 /////")
time.sleep(0.5)
print("Year 2014 : " + str(sum14) + "/" + str(count) + " = " + "{:.2f}".format(round(sum14/count, 2)))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + "{:.2f}".format(round(mean(lst0114), 2)))
    
    print("\tMonth 2 : " + "{:.2f}".format(round(mean(lst0214), 2)))
    
    print("\tMonth 3 : " + "{:.2f}".format(round(mean(lst0314), 2)))
    
    print("\tMonth 4 : " + "{:.2f}".format(round(mean(lst0414), 2)))
    
    print("\tMonth 5 : " + "{:.2f}".format(round(mean(lst0514), 2)))
    
    print("\tMonth 6 : " + "{:.2f}".format(round(mean(lst0614), 2)))
    
    print("\tMonth 7 : " + "{:.2f}".format(round(mean(lst0714), 2)))
    
    print("\tMonth 8 : " + "{:.2f}".format(round(mean(lst0814), 2)))
    
    print("\tMonth 9 : " + "{:.2f}".format(round(mean(lst0914), 2)))
    
    print("\tMonth 10 : " + "{:.2f}".format(round(mean(lst1014), 2)))
    
    print("\tMonth 11 : " + "{:.2f}".format(round(mean(lst1114), 2)))
    
    print("\tMonth 12 : " + "{:.2f}".format(round(mean(lst1214), 2)))
time.sleep(0.5)
print("Year 2015 : " + str(sum15) + "/" + str(count) + " = " + "{:.2f}".format(round(sum15/count, 2)))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + "{:.2f}".format(round(mean(lst0115), 2)))
    
    print("\tMonth 2 : " + "{:.2f}".format(round(mean(lst0215), 2)))
    
    print("\tMonth 3 : " + "{:.2f}".format(round(mean(lst0315), 2)))
    
    print("\tMonth 4 : " + "{:.2f}".format(round(mean(lst0415), 2)))
    
    print("\tMonth 5 : " + "{:.2f}".format(round(mean(lst0515), 2)))
    
    print("\tMonth 6 : " + "{:.2f}".format(round(mean(lst0615), 2)))
    
    print("\tMonth 7 : " + "{:.2f}".format(round(mean(lst0715), 2)))
    
    print("\tMonth 8 : " + "{:.2f}".format(round(mean(lst0815), 2)))
    
    print("\tMonth 9 : " + "{:.2f}".format(round(mean(lst0915), 2)))
    
    print("\tMonth 10 : " + "{:.2f}".format(round(mean(lst1015), 2)))
    
    print("\tMonth 11 : " + "{:.2f}".format(round(mean(lst1115), 2)))
    
    print("\tMonth 12 : " + "{:.2f}".format(round(mean(lst1215), 2)))
time.sleep(0.5)
print("Year 2016 : " + str(sum16) + "/" + str(count) + " = " + "{:.2f}".format(round(sum16/count, 2)))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + "{:.2f}".format(round(mean(lst0116), 2)))
    
    print("\tMonth 2 : " + "{:.2f}".format(round(mean(lst0216), 2)))
    
    print("\tMonth 3 : " + "{:.2f}".format(round(mean(lst0316), 2)))
    
    print("\tMonth 4 : " + "{:.2f}".format(round(mean(lst0416), 2)))
    
    print("\tMonth 5 : " + "{:.2f}".format(round(mean(lst0516), 2)))
    
    print("\tMonth 6 : " + "{:.2f}".format(round(mean(lst0616), 2)))
    
    print("\tMonth 7 : " + "{:.2f}".format(round(mean(lst0716), 2)))
    
    print("\tMonth 8 : " + "{:.2f}".format(round(mean(lst0816), 2)))
    
    print("\tMonth 9 : " + "{:.2f}".format(round(mean(lst0916), 2)))
    
    print("\tMonth 10 : " + "{:.2f}".format(round(mean(lst1016), 2)))
    
    print("\tMonth 11 : " + "{:.2f}".format(round(mean(lst1116), 2)))
    
    print("\tMonth 12 : " + "{:.2f}".format(round(mean(lst1216), 2)))

#Display Median Section
lst14.sort(), lst0114.sort(), lst0214.sort(), lst0314.sort(), lst0414.sort(), lst0514.sort(), lst0614.sort(), lst0714.sort(), lst0814.sort(), lst0914.sort(), lst1014.sort(), lst1114.sort(), lst1214.sort()
lst15.sort(), lst0115.sort(), lst0215.sort(), lst0315.sort(), lst0415.sort(), lst0515.sort(), lst0615.sort(), lst0715.sort(), lst0815.sort(), lst0915.sort(), lst1015.sort(), lst1115.sort(), lst1215.sort()
lst16.sort(), lst0116.sort(), lst0216.sort(), lst0316.sort(), lst0416.sort(), lst0516.sort(), lst0616.sort(), lst0716.sort(), lst0816.sort(), lst0916.sort(), lst1016.sort(), lst1116.sort(), lst1216.sort()
time.sleep(0.5)
print("\n ///// MEDIAN FROM ALL REGION EACH MONTH FROM 2014 - 2016 /////")
time.sleep(0.5)
print("Year 2014 : " + str(lst14[count//2]))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + str(lst0114[5]))
    
    print("\tMonth 2 : " + str(lst0214[5]))
    
    print("\tMonth 3 : " + str(lst0314[5]))
    
    print("\tMonth 4 : " + str(lst0414[5]))
    
    print("\tMonth 5 : " + str(lst0514[5]))
    
    print("\tMonth 6 : " + str(lst0614[5]))
    
    print("\tMonth 7 : " + str(lst0714[5]))
    
    print("\tMonth 8 : " + str(lst0814[5]))
    
    print("\tMonth 9 : " + str(lst0914[5]))
    
    print("\tMonth 10 : " + str(lst1014[5]))
    
    print("\tMonth 11 : " + str(lst1114[5]))
    
    print("\tMonth 12 : " + str(lst1214[5]))
time.sleep(0.5)
print("Year 2015 : " + str(lst15[count//2]))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + str(lst0115[5]))
    
    print("\tMonth 2 : " + str(lst0215[5]))
    
    print("\tMonth 3 : " + str(lst0315[5]))
    
    print("\tMonth 4 : " + str(lst0415[5]))
    
    print("\tMonth 5 : " + str(lst0515[5]))
    
    print("\tMonth 6 : " + str(lst0615[5]))
    
    print("\tMonth 7 : " + str(lst0715[5]))
    
    print("\tMonth 8 : " + str(lst0815[5]))
    
    print("\tMonth 9 : " + str(lst0915[5]))
    
    print("\tMonth 10 : " + str(lst1015[5]))
    
    print("\tMonth 11 : " + str(lst1115[5]))
    
    print("\tMonth 12 : " + str(lst1215[5]))
time.sleep(0.5)
print("Year 2016 : " + str(lst16[count//2]))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + str(lst0116[5]))
    
    print("\tMonth 2 : " + str(lst0215[5]))
    
    print("\tMonth 3 : " + str(lst0315[5]))
    
    print("\tMonth 4 : " + str(lst0416[5]))
    
    print("\tMonth 5 : " + str(lst0516[5]))
    
    print("\tMonth 6 : " + str(lst0616[5]))
    
    print("\tMonth 7 : " + str(lst0716[5]))
    
    print("\tMonth 8 : " + str(lst0816[5]))
    
    print("\tMonth 9 : " + str(lst0916[5]))
    
    print("\tMonth 10 : " + str(lst1016[5]))
    
    print("\tMonth 11 : " + str(lst1116[5]))
    
    print("\tMonth 12 : " + str(lst1216[5]))

#Dispaly Mode Section       !!!No Mode
time.sleep(0.5)
print("\n ///// MODE FROM ALL REGION EACH MONTH FROM 2014 - 2016 /////")
time.sleep(0.5)
print(" !!! NO MODE FROM THIS DATASET\n\t: EACH DATA ARE IDENTICAL")

#Dispaly S.D. Section
time.sleep(0.5)
print("\n ///// S.D. FROM ALL REGION EACH MONTH FROM 2014 - 2016 /////")
time.sleep(0.5)
print("Year 2014 : " + "{:.2f}".format(round(findSD(lst14), 2)))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + "{:.2f}".format(round(findSD(lst0114), 2)))
    
    print("\tMonth 2 : " + "{:.2f}".format(round(findSD(lst0214), 2)))
    
    print("\tMonth 3 : " + "{:.2f}".format(round(findSD(lst0314), 2)))
    
    print("\tMonth 4 : " + "{:.2f}".format(round(findSD(lst0414), 2)))
    
    print("\tMonth 5 : " + "{:.2f}".format(round(findSD(lst0514), 2)))
    
    print("\tMonth 6 : " + "{:.2f}".format(round(findSD(lst0614), 2)))
    
    print("\tMonth 7 : " + "{:.2f}".format(round(findSD(lst0714), 2)))
    
    print("\tMonth 8 : " + "{:.2f}".format(round(findSD(lst0814), 2)))
    
    print("\tMonth 9 : " + "{:.2f}".format(round(findSD(lst0914), 2)))
    
    print("\tMonth 10 : " + "{:.2f}".format(round(findSD(lst1014), 2)))
    
    print("\tMonth 11 : " + "{:.2f}".format(round(findSD(lst1114), 2)))
    
    print("\tMonth 12 : " + "{:.2f}".format(round(findSD(lst1214), 2)))
time.sleep(0.5)
print("Year 2015 : " + "{:.2f}".format(round(findSD(lst15), 2)))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + "{:.2f}".format(round(findSD(lst0115), 2)))
    
    print("\tMonth 2 : " + "{:.2f}".format(round(findSD(lst0215), 2)))
    
    print("\tMonth 3 : " + "{:.2f}".format(round(findSD(lst0315), 2)))
    
    print("\tMonth 4 : " + "{:.2f}".format(round(findSD(lst0415), 2)))
    
    print("\tMonth 5 : " + "{:.2f}".format(round(findSD(lst0515), 2)))
    
    print("\tMonth 6 : " + "{:.2f}".format(round(findSD(lst0615), 2)))
    
    print("\tMonth 7 : " + "{:.2f}".format(round(findSD(lst0715), 2)))
    
    print("\tMonth 8 : " + "{:.2f}".format(round(findSD(lst0815), 2)))
    
    print("\tMonth 9 : " + "{:.2f}".format(round(findSD(lst0915), 2)))
    
    print("\tMonth 10 : " + "{:.2f}".format(round(findSD(lst1015), 2)))
    
    print("\tMonth 11 : " + "{:.2f}".format(round(findSD(lst1115), 2)))
    
    print("\tMonth 12 : " + "{:.2f}".format(round(findSD(lst1215), 2)))
time.sleep(0.5)
print("Year 2016 : " + "{:.2f}".format(round(findSD(lst16), 2)))
if mode in ('A', 'a') :
    
    print("\tMonth 1 : " + "{:.2f}".format(round(findSD(lst0116), 2)))
    
    print("\tMonth 2 : " + "{:.2f}".format(round(findSD(lst0216), 2)))
    
    print("\tMonth 3 : " + "{:.2f}".format(round(findSD(lst0316), 2)))
    
    print("\tMonth 4 : " + "{:.2f}".format(round(findSD(lst0416), 2)))
    
    print("\tMonth 5 : " + "{:.2f}".format(round(findSD(lst0516), 2)))
    
    print("\tMonth 6 : " + "{:.2f}".format(round(findSD(lst0616), 2)))
    
    print("\tMonth 7 : " + "{:.2f}".format(round(findSD(lst0716), 2)))
    
    print("\tMonth 8 : " + "{:.2f}".format(round(findSD(lst0816), 2)))
    
    print("\tMonth 9 : " + "{:.2f}".format(round(findSD(lst0916), 2)))
    
    print("\tMonth 10 : " + "{:.2f}".format(round(findSD(lst1016), 2)))
    
    print("\tMonth 11 : " + "{:.2f}".format(round(findSD(lst1116), 2)))
    
    print("\tMonth 12 : " + "{:.2f}".format(round(findSD(lst1216), 2)))

#Graph Plot !!!!!WAITING TO ADD REAL DATA
#pltA.figure(figsize=(8,4))
print("\n. . . Plotting Graphs . . .")
'''
x, y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[1:13]
a, b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[13:25]
c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[25:37]
e, f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[37:49]
g, h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[49:61]
k, l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[61:73]
m, n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[73:85]
o, p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14[85:95]
pltA.plot(x, y, label = "Africa", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(a, b, label = "Americas", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(c, d, label = "Asean", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(e, f, label = "East Asia", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(g, h, label = "Europe", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(k, l, label = "Middle East", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(m, n, label = "Oceania", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(o, p, label = "South Asia", marker = 'o', markerfacecolor = 'green', markersize = 5)
#naming
pltA.xlabel('Number of Tourist')
pltA.ylabel('Month')
pltA.title('Tourism in Thailand 2014 each month')
'''
'''
#Line graph
x, y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst14E[0:12]
a, b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst15E[0:12]
c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lst16E[0:12]
pltA.plot(x, y, label = "Yr2014", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(a, b, label = "Yr2015", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.plot(c, d, label = "Yr2016", marker = 'o', markerfacecolor = 'green', markersize = 5)
pltA.xlabel('Number of Tourist')
pltA.ylabel('Month')
pltA.title('Tourism in Thailand 2014 - 2016')
#show the plot
pltA.legend()
pltA.show()
'''

#Scatter plot
months_range = [ i for i in range(1,13)]
plt0.scatter(months_range, lst15E)
plt0.title('2015 Tourist visit Thailand Each month')
plt0.xlabel('Month')
plt0.ylabel('Volume of tourists (People)')
plt0.show()

plt1.scatter(months_range, lst16E)
plt1.title('2016 Tourist visit Thailand Each month')
plt1.xlabel('Month')
plt1.ylabel('Volume of tourists (People)')
plt1.show()

#Box plot
data = [lst15E, lst16E]
fig = pltB.figure()
pltB.boxplot(data)
pltB.title('2015 & 2016 Tourist visit Thailand')
plt1.xlabel('Year 2015 & 2016')
plt1.ylabel('Volume of tourists (People)')
pltB.show()

#Histogram
plt2.hist(lst15E, density = 1, bins = 20)
plt2.title('2015 Tourist')
plt2.show()

plt3.hist(lst16E, density = 1, bins = 20)
plt3.title('2016 Tourist')
plt3.show()

#Stem & leaf   !!!Not Recommend with this data
#print(lst14E)