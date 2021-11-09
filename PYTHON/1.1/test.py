from file_reader_module import readFile
import matplotlib.pyplot as plt

excel = readFile('film.csv')
#list for the films year
years = []
for i in excel:
#films year
    if excel[i]['Release_year'] not in years:
        years.append(excel[i]['Release_year'])
#make dictionaries with the list information
yearDictionary = {}
for j in years:
    yearDictionary[j] = 0

for i in range(len(excel)):
    if excel[i]['Release_year'] in yearDictionary:
        yearDictionary[excel[i]['Release_year']] += 1

year_as = []
quantity_as = []
for i in yearDictionary:
    year_as.append(i)
    quantity_as.append(yearDictionary[i])



#must be the years
#names = ['michael','papi','liendo','carlos']
#must be the quantity films
#scores = [89,90,22,44]
#scores2 = [95,85,20,59]
#positions = [0,1,2,3]
#positions2 = [0.3,1.3,2.3,3.3]
#positions3 = [0.15,1.15,2.15,3.15]
#plt.bar(positions, scores,width=0.3)
#plt.bar(positions2,scores2,width=0.3)
#plt.xticks(positions3,names)