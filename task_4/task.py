import json
import configparser

config = configparser.ConfigParser()

config.read('config')

list_1 = json.loads(config['DEFAULT']['list_1'])
list_2 = json.loads(config['DEFAULT']['list_2'])

for value in list_1:
    if value in list_2:
        print(value)
#other manual way
#similar = [value for value in list_1 if value in list_2]
#print(similar)

#python methods
#print(set(list_1))
#print(list(set(list_1).intersection(list_2)))