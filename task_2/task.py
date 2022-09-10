import configparser
import json

config = configparser.ConfigParser()

config.read('config')

array = json.loads(config['DEFAULT']['array'])

#python methods
#print(sum(array))

#manual 
s=0 
for i in array:
    s+=i
print(s)