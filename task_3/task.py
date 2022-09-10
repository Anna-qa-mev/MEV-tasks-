import configparser
import json
import sys

config = configparser.ConfigParser()

config.read('config')

config_array = config['DEFAULT']['array']

array = json.loads(config_array)

# python methods
print(min(array))
print(max(array))

# manual
min_value = sys.maxsize
max_value = -sys.maxsize

for value in array:
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value

print(min_value, max_value)
