import csv
import collections
#import numpy as np
proteinNums=[]
for i in range(1,19):
    if len(str(i))==1:
        proteinNums.append('~50' + str(i) + '~')
    else:
        proteinNums.append('~5' + str(i) + '~')

arrOfArr=[]
#rowArr=[]
#print proteinNums
counter=0
with open('NUT_DATA.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='^')

    for row in spamreader:
        for number in proteinNums:
           if number in row:
               rowArr=[]
               counter += 1
              # print rowArr
              # print counter

               rowArr.append(row[0])
               rowArr.append(row[1])
               rowArr.append(row[2])
              # print rowArr
               arrOfArr.append(rowArr)

# print(arrOfArr)
#for row in arrOfArr:
    #print row

myDict=dict()

for key in arrOfArr:

    #print key[2]
    if key[0] in myDict:
        myDict[key[0]]=myDict[key[0]]+([key[1] , key[2]])
    else:
        myDict[key[0]]=[key[1], key[2]]


    #if i[0] in myDict:
    #    myDict[i[0]] = appendDict.append(i[2])
    #else:
    #    appendDict=[]
    #    myDict[i[0]] = appendDict.append(i[2])


od = collections.OrderedDict(sorted(myDict.items()))
print od

#for i in xrange(100):
#    key = i % 10
#    if key in d:
#        d[key] += 2
#    else:
#        d[key] = 1


#print(d)
#for i in arrOfArr:
#    if i[0]
