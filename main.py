
''' The 1st objective is to read a similar JSON file as that of ./data. 
But the catch here is, i dont have any similar to read from. Therefore, i will have to create a similar
JSON file to read from. '''

#importing the JSON module
import json

#The Draft&Validator module validates the schema to the entry data
from jsonschema import Draft7Validator

#Importing the schema.json file to the main.py workspace for data validation
with open('schema.json') as schema_file:

  #This loads the schema file and stored into my_schema
  my_schema = json.load(schema_file)

#Creating the JSON document
assessment_data = """{
  "message": {
      "battle": {
        "id": "ABCDEFGHIJKLMNOPQR",
        "name": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "orientation": "ABCDEFGHIJKLMNO",
        "settings": {
          "minParticipants": 942,
          "maxParticipants": 641,
          "battleType": "ABCDEFGHIJKLMN",
          "wagerType": "ABCDEFGHIJKLMNOPQRSTUVW",
          "countdown": 69,
          "duration": 200,
          "archetype": {
            "name": "ABCDEFGHIJKLMNOPQRS",
            "iconId": "ABCDEFGHIJKLMNOPQRST"
          }
        },
        "status": "ABCDEFGHIJKL",
        "creationTime": 240,
        "startTime": 626,
        "endTime": 353,
        "creator": {
          "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
          "nickname": "ABCDEFGHIJKLMNOPQ",
          "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "accountType": "ABCDE",
          "countryCode": "ABCD",
          "orientation": "ABCDEFGHIJKLMNO"
        },
        "tag" : "active"
      },
        "participants": [
          {
            "user": {
              "id": "ABCDEFGHIJKLMN",
              "nickname": "ABCDEFGHIJKLMN",
              "title": "ABCDEFGHIJK",
              "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
              "countryCode": "ABCDEFGH",
              "orientation": "ABCDEFGHIJKLMNOPQRSTUVWXY"
            },
            "creator": False,
            "ranking": 498,
            "numberOfTrades": 862,
            "performance": "ABCDEFGHIJKLMNOPQRSTUVW"
          }
        ],
        "tag" : ["ABCD", "EFGH"]
      },
      "joiner": {
        "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZAB",
        "nickname": "ABCDEFGHIJKLMNO",
        "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
        "accountType": "ABCDEFGHIJKLMNOPQRS",
        "countryCode": "ABCDEFGHIJKLMNOPQR",
        "orientation": "ABCDEFGHIJKLMNOPQR",
        "tag" : ["dgvbjk", "qwerty"]
      },
      "participantIds": {[
        "ABCDEFGHIJKLMNOPQRST", "ABCDEFGHIJKLMNOPQRSTUVWXY" ]
      },
    
} """
 
 #Creating a directory for storing the json data and storing it in variable "file" for reuse.
#This code will only be use once. Once the file has been created, then it can be remove 
file =  open("C:/Users/LORD MUFI/Desktop/Python Engineer JSON Assessment/similar data.json", "w")

#Using dump to save the json data into a file. Indent is used to avoid long plain format.
#The sort_key attribute sort the data in alphabetical order.
json.dump(assessment_data, file, indent=3)


#Validation and testing. If no error, then the schema matches the data
validator = Draft7Validator(my_schema)

#This print entries that does not matches the schema constraints as error
print(list(validator.iter_errors(assessment_data)))


