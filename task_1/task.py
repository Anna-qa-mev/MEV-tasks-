import configparser

config = configparser.ConfigParser()

config.read('config')

age = 0
stable_hr = 0

try:
    age = int(config['DEFAULT']['age'])
    stable_hr = config['DEFAULT']['stable_hr']
    # check that age is in valid range
    # check stable_hr range
except Exception as e: 
    print(e)
    

max_hr = 220 - age

keypoints = [50, 60, 70, 80, 90, 100]
names = ["Recovery", "Light", "Aerobic", "Anaerobic", "Max"]

for zone_name, previous, current in zip(names, keypoints, keypoints[1:]):
    print("{} {:d}%-{:d}% {:d} {:d}".format(zone_name, previous, current, int(previous * max_hr / 100), int(current * max_hr / 100)))
