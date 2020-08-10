import os
import requests
import time

if not os.path.exists("json/"):
    os.mkdir("json/")
    print("json Directory Created ")

QuestReward = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/QuestReward.json'
r = requests.get(QuestReward, allow_redirects=True)
if open('json/QuestReward.json', 'wb').write(r.content):
    try:
        print("QuestReward has been updated")
        time.sleep(1)
    except:
        print("could not update QuestReward")
        time.sleep(1)

QuestRewardType = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/QuestRewardType.json'
r = requests.get(QuestRewardType, allow_redirects=True)
if open('json/QuestRewardType.json', 'wb').write(r.content):
    try:
        print("QuestRewardType has been updated")
        time.sleep(1)
    except:
        print("could not update QuestRewardType")
        time.sleep(1)

Pokemon = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Pokemon.json'
r = requests.get(Pokemon, allow_redirects=True)
if open('json/Pokemon.json', 'wb').write(r.content):
    try:
        print("Pokemon has been updated")
        time.sleep(1)
    except:
        print("could not update Pokemon")
        time.sleep(1)

Form = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Form.json'
r = requests.get(Form, allow_redirects=True)
if open('json/Form.json', 'wb').write(r.content):
    try:
        print("Form has been updated")
        time.sleep(1)
    except:
        print("could not update Form")
        time.sleep(1)

Costume = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Costume.json'
r = requests.get(Costume, allow_redirects=True)
if open('json/Costume.json', 'wb').write(r.content):
    try:
        print("Costume has been updated")
        time.sleep(1)
    except:
        print("could not update Costume")
        time.sleep(1)