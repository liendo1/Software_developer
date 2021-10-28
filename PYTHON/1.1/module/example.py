import csv

dataBase = {}
idCounter = 0
# unique id for the count
idList = []
# list for the ratings
ratings = []
# list for the films year
years = []
# list of actors name
actorName = []
file = open('film.csv', 'r')
d_reader = csv.DictReader(file, delimiter=';')
for i in d_reader:
    # append only unique id
    if i['film_id'] not in idList:
        idList.append(i['film_id'])
    # rating
    if i['rating'] not in ratings:
        ratings.append(i['rating'])
    # films year
    if i['release_year'] not in years:
        years.append(i['release_year'])
    # actor names
    if i['actor_name'] not in actorName:
        actorName.append(i['actor_name'])

    dataBase[i['film_id']] = {}
    dataBase[i['film_id']]['Film_id'] = i['film_id']
    dataBase[i['film_id']]['Title'] = i['title']
    dataBase[i['film_id']]['Release_year'] = i['release_year']
    dataBase[i['film_id']]['Rating'] = i['rating']
    dataBase[i['film_id']]['Actor_name'] = i['actor_name']

# make dictionaries with the list information
idDictionary = {}
ratingDictionary = {}
yearDictionary = {}
actorDictionary = {}

for j in idList:
    idDictionary[j] = 0
for j in ratings:
    ratingDictionary[j] = 0
for j in years:
    yearDictionary[j] = 0
for j in actorName:
    actorDictionary[j] = 0

# films per rating
for info in dataBase:
    print(dataBase[info]['Rating'])

    # if i['actor_name'] == 'Adam Grant':

    # excel[i['film_id']]={"Film_id":i['film_id'],"Title":i['title'],"Release_year":i['release_year'],"Rating":i['rating'],
    # "Actor_name":i['actor_name']}

# print(counter)
# count = 0

# for key, value in excel.items():
#   if value['Actor_name'] == 'Adam Grant':
#      print(key, ":", value['Title'],value['Actor_name'])
#     count+=1

# print(len(excel))