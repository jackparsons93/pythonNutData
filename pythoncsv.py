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
        myDict[key[0]]=myDict[key[0]]+[[key[1] , key[2]]]
    else:
        myDict[key[0]]=[[key[1], key[2]]]


    #if i[0] in myDict:
    #    myDict[i[0]] = appendDict.append(i[2])
    #else:
    #    appendDict=[]
    #    myDict[i[0]] = appendDict.append(i[2])


od = collections.OrderedDict(sorted(myDict.items()))
#print od
aminoDict=collections.OrderedDict()
count=0
for value in od:
    #print(value) # + str(od[value]))
    count=0
    aminoTotal=0.0
    for amino in od[value]:
        #print(str(od[value][count][1]))
        #print('****************')
        aminoTotal=float(od[value][count][1])+aminoTotal
        count += 1
        
    print aminoTotal
    aminoDict[value]=aminoTotal

    #print(count)
#print str(od['~05306~'])
#print(aminoDict)


for value in od:
    print(value) # + str(od[value]))
    count=0
    
    for amino in od[value]:
        aminoPercentage=0
        #print(str(od[value][count][1]))
        #print('****************')
        #aminoTotal=float(od[value][count][1])+aminoTotal
        try:
            aminoPercentage= (float(od[value][count][1]))/aminoDict[value]*100
            print(aminoPercentage)
            count += 1
        except ZeroDivisionError:
            print("Divided by zero??")
            print(value+str(od[value]))
            count += 1
        
    #print aminoTotal
    #aminoDict[value]=aminoTotal
wheyDictPercent=collections.OrderedDict()
#typtophan
wheyDictPercent["~501~"]=1.4
#Threonine
wheyDictPercent["~502~"]=6.7
#Isoleucine
wheyDictPercent["~503~"]=6.4
#Leucine
wheyDictPercent["~504~"]=10.6
#Lysine
wheyDictPercent["~505~"]=9.6
#Methione
wheyDictPercent["~506~"]=2.2
#cystine
wheyDictPercent["~507~"]=2.2
#Phenylalanine
wheyDictPercent["~508~"]=3.0
#Tyrosine
wheyDictPercent["~509~"]=2.6
#Valine
wheyDictPercent["~510~"]=5.9
#arginine
wheyDictPercent["~511~"]=2.1
#Histidine
wheyDictPercent["~512~"]=1.7
#Alanine
wheyDictPercent["~513~"]=5.0
#Aspartic Acid
wheyDictPercent["~514~"]=11.0
#Glutamic Acid
wheyDictPercent["~515~"]=18.1
#Glycine
wheyDictPercent["~516~"]=1.4
#proline
wheyDictPercent["~517~"]=5.5
#serine
wheyDictPercent["~518~"]=4.6


print(sum(wheyDictPercent.values()))

#print(1.11153945001+4.04137753791+4.44615780005+7.87715240298+8.08275507582+3.1290156772+1.31071703932+3.83577486507+3.23181701362+4.14417887433+7.07401696222+2.01747622719+5.85967617579+10.100231303+15.3559496273+11.3145720894+3.1290156772+3.93857620149)

#def dictBuilder(odInput):




#for i in xrange(100):
#    key = i % 10
#    if key in d:
#        d[key] += 2
#    else:
#        d[key] = 1


#print(d)
#for i in arrOfArr:
#    if i[0]
