import json
import configparser

config = configparser.ConfigParser()

config.read('config')

some_text = config['DEFAULT']['some_text']
#print(some_text)

text = some_text.replace(',', '').replace('.', '').lower()
#print(text)
#python methods
words = text.split()

unique_words = set(words)
#print(words)

for unique_word in unique_words:
    print(unique_word, words.count(unique_word))
#manual 
"""
counts = dict()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
"""