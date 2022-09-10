import configparser

config = configparser.ConfigParser()

config.read('config')

some_text = config['DEFAULT']['some_text']

#python methods
#text = some_text.replace(" ","")
#print(text)

#manual
result_str= ''
for s in some_text:
    if s!=' ':
        result_str += s

print(result_str)