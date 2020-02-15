import math

all = [98.94, 98.93, 98.93]
entryNum=0
for x in all:
    entryNum += 1

A = entryNum
ave = 0.0
tot = 0

for p in range(0, entryNum):
    tot = tot + float(all[p])

ave = tot / entryNum


sigmaSum = 0
for d in range(0, entryNum):
    sigmaSum = sigmaSum + ((float(all[d]) - float(ave))**2)

w = math.sqrt((1/(entryNum-1)) * float(sigmaSum))

wm = w/(math.sqrt(entryNum))

toolError = (ave * (0.05/100)) + 0.1
if(wm < (toolError * (1/10))):
    print("Use tool accuracy for error.")
else:
    print("Use standard deviation of the mean for error.")
print("Entry number: " + str(A))
print("Standard Deviation: " + str(w))
print("SD of the mean: " + str(wm))
print("Error of average with tool error: " + str(toolError))
print("Average: " + str(ave))
