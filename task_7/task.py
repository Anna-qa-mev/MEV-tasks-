import configparser
from platform import python_branch

config = configparser.ConfigParser()

config.read('config')

str = config['DEFAULT']['str']
rev_string = str[::-1]
#print(rev_string)

is_palindrome = True

"""
for index in range(0, len(str) // 2):
    if str[index] != str[len(str) - 1 - index]:
        is_palindrome = False
        break
"""

if str == rev_string:
#if is_palindrome:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")

#print("this is pslindrome")
