#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import createMessage
import sql
import sendMessage
import sys
import time
import clear
import os
import json

####Lade das Configfile
cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("config.ini")

if not os.path.exists(cfg.areaName+cfg.areaNumber):
    os.mkdir(cfg.areaName+cfg.areaNumber)
    print("Temp Directory " , cfg.areaName+cfg.areaNumber ,  " Created ")
else:    
    print("Temp Directory " , cfg.areaName+cfg.areaNumber ,  " already exists")

if not os.path.exists(cfg.areaName+cfg.areaNumber+"/values.json"):
  f = open(cfg.areaName+cfg.areaNumber+"/values.json", "w")
  f.write("{\n")
  f.write('   "stardust": [1500,1000,500],\n')
  f.write('   "item": [502,503,504,708,1301],\n')
  f.write('   "pokemon": [129,114,453,50,204,185,1]\n')
  f.write("}")
  f.close()

clear = clear.Clear()
clear.clear(cfg.token,cfg.chatId,cfg.singlechatId,cfg)

send = sendMessage.sendMessage()
send.setConfig(cfg.token,cfg.singlechatId,cfg.chatId,cfg.areaName,cfg.areaNumber)
sys.stdout.write("\x1b]2;%s\x07" % cfg.areaName+cfg.areaNumber)

while 1 == 1:
  with open(cfg.areaName+cfg.areaNumber+"/values.json") as input:
    values = json.load(input)

  Sql = sql.Sql()
  Sql.startSQL(cfg,values)
  send.clearOutputList(Sql.pokestop_id)
  create = createMessage.createMessage()
  create.create(Sql,send,cfg.sleepTime,cfg,values)
  time.sleep(int(cfg.sleepTime))