from textwrap import indent
import requests
import json
url = 'https://zoo-animal-api.herokuapp.com/animals/rand'
list = []
for i in range(10):
    randomRequests = requests.get(url).json()
    list.append(randomRequests)

dictionary={}
dictionary['practice'] = list

jsonAnimalObjejct = json.dumps(dictionary, indent=4)
jsonAnimalFile = open('animal.json', 'w')
jsonAnimalFile.write(jsonAnimalObjejct)
jsonAnimalFile.close()

jsonData = open('animal.json', 'r', encoding='utf-8')
animalData = json.load(jsonData)
jsonData.close()

# I am going to sort information of animals
listAnimal = animalData['practice']
l = len(listAnimal)
newListAnimalData = []
for i in range(l):
    oneAnimalData = {}
    oneAnimalData['animalName'] = listAnimal[i]['name'] 
    oneAnimalData['animalType'] = listAnimal[i]['animal_type']
    oneAnimalData['imageLink'] = listAnimal[i]['image_link']
    oneAnimalData['lifeSpan'] = listAnimal[i]['lifespan']
    newListAnimalData.append(oneAnimalData)

newAnimalData = {}
newAnimalData['dataOfSeveralAnimals'] = newListAnimalData

writeJson = json.dumps(newAnimalData, indent=4)
newAnimal = open('newAnimal.json', 'w')
newAnimal.write(writeJson)
newAnimal.close()