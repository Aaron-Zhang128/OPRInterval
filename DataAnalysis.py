import pandas as pd
import csv
import math
df = pd.read_csv("data.csv")
print(df)
final = {}
# for i in df["Red"]:
#     if i not in final:
#         final[i] = df[""]

length = len(df["Red"])

counter = 0

while counter < length:
    # print(df["Red1"][counter])
    x = df["Red1"][counter]
    print(x)
    if x not in final:
    #     final[int(df["Red1"][counter])] = final[int(df["R1"][counter])]
        final[x] = [int(df["R1"][counter])]
    else:
        final[x] = final[x] + [int(df["R1"][counter])]
    counter = counter + 1
    
    
counter = 0

while counter < length:
    # print(df["Red1"][counter])
    x = df["Red2"][counter]
    print(x)
    if x not in final:
    #     final[int(df["Red1"][counter])] = final[int(df["R1"][counter])]
        final[x] = [int(df["R2"][counter])]
    else:
        final[x] = final[x] + [int(df["R2"][counter])]
    counter = counter + 1
    
    
    
counter = 0
while counter < length:
    # print(df["Red1"][counter])
    x = df["Blue1"][counter]
    print(x)
    if x not in final:
    #     final[int(df["Red1"][counter])] = final[int(df["R1"][counter])]
        final[x] = [int(df["B1"][counter])]
    else:
        final[x] = final[x] + [int(df["B1"][counter])]
    counter = counter + 1   
    
    
counter = 0
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
while counter < length:
    # print(df["Red1"][counter])
    x = df["Blue2"][counter]
    print(x)
    if x not in final:
    #     final[int(df["Red1"][counter])] = final[int(df["R1"][counter])]
        final[x] = [int(df["B2"][counter])]
    else:
        final[x] = final[x] + [int(df["B2"][counter])]
    counter = counter + 1   
print(final)

f = open("output.txt", "a")

for i in final:
    
    # print(i)
    theList = final[i]
    sum = 0
    for j in theList:
        sum = sum + j
    mean = sum/len(theList)
    ja = 0
    for k in theList:
        ja = ja + (k - mean)**2
        
    standardDeviation = math.sqrt(ja/(len(theList)-1))
    if len(theList) == 5:
        t = 2.1318
    elif len(theList) == 6:
        t = 2.0150
    elif len(theList) == 7:
        t = 1.94318
    
    
    lower = mean - t * standardDeviation/ math.sqrt(len(theList))
    higher = mean + t * standardDeviation/ math.sqrt(len(theList))
    output = str(i) + "," + str(lower) + "," + str(higher) + "\n"
    # with open('output.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.append([i,lower,higher])
    # # print(i)

    f.write(output)
f.close() 
        
    

    
    
t = 0
t5 = 2.7764
t6 = 2.5705
t7 = 2.4469