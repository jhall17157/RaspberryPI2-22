import datetime as dt
import requests
import json
from gpiozero import Button
from time import sleep
import random

t = dt.datetime.now()
location = random.randint(0,4)
t_json = "{0}-{1}-{2}T{3}:{4}:{5}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H"), t.strftime("%M"), t.strftime("%S"))
filename = "/home/pi/{}.txt".format(t.strftime("%Y-%m-%d"))
try :
    f = open(filename, "r")
except:
    f = open(filename, "x")
#print(t.strftime("D: %Y-%m-%d T: %H:%M:%S"), location)

def log():
    # create a new event - replace with your API
    url = 'https://modas-jsg.azurewebsites.net/api/event/'
    headers = { 'Content-Type': 'application/json'}
    payload = { 'timestamp': t_json, 'flagged': False, 'locationId': location }
    # post the event
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(r.status_code)
    print(r.json())
    
    f = open(filename, "a")
    f.write(repr(r.json()))
    f.write(repr(r.status_code))
    f.write("\n")
    f.close()
    
    
button = Button(8)
button.when_released = log

try:
    # program loop
    while True:
        sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
    print("goodbye")