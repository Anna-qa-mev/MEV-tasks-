import configparser

config = configparser.ConfigParser()

config.read('config')

password = config['DEFAULT']['pw']
import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
result = re.findall(pattern, password)
if (result):
    print ("Strong password")
else:
    print ("Password is not strong enough")