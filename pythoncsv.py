import csv

proteinNums=[]
for i in range(1,19):
    if len(str(i))==1:
        proteinNums.append('~50' + str(i) + '~')
    else:
        proteinNums.append('~5' + str(i) + '~')


print proteinNums
with open('NUT_DATA.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='^')

    for row in spamreader:
        for number in proteinNums:
           if number in row:
               print row[1] , row[2]
